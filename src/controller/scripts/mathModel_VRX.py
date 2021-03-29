#!/usr/bin/env/python3

# Math model of WAMV for differential thrust using Fossen 7.3.2:Linearized DP Model

import rospy
import math
import numpy as np

from std_msgs.msg import String
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry
from geometry_msgs.msg import AccelWithCovarianceStamped

rospy.init_node("math_model")

################################################################################
# PARAMETER DEFINITIONS
################################################################################
# WAMV characteristics (From VRX GitHub: vrx/wamv_description/urdf/wamv_base.urdf.xacro)
mass = 180.0
Iz = 446.0
# Hydrodynamic damping coefficients (From VRX GitHub: vrx/wamv_gazebo/urdf/dynamics/wamv_gazebo_dynamics_plugin.xacro)
Xu = 51.3
Yv = 40.0
Nr = 400.0
Yr = 0.0
Nv = 0.0
# Added mass coefficients (From VRX GitHub: vrx/wamv_gazebo/urdf/dynamics/wamv_gazebo_dynamics_plugin.xacro)
Xudot = 0.0
Yvdot = 0.0
Nrdot = 0.0
Yrdot = 0.0
# Other parameters
xg = 0.0        # Distance between base_link and COG in x-direction
xp = 2.373776   # Thruster offset from base_link in x-direction (from thruster config)
yp = 1.027135   # Thruster offset from base_link in y-direction (from thruster config)
B = np.array([(1,1), (0,0), (yp,-yp)])  # Thruster config for differential thrust, +z down
u = np.transpose(np.array([0,0]))       # Thruster command input vector, [T_p, T_s]^T
b = np.transpose(np.array([0.0,0.0,0.0]))           # Current in inertial frame
tau_wind = np.transpose(np.array([0.0,0.0,0.0]))    # Environmental wind forces
tau_wave = np.transpose(np.array([0.0,0.0,0.0]))    # Environmental wave forces
psi = 0.0       # Angle between WAMV heading and inertial frame (NED) for current's rotation matrix
R_psi = np.array([(math.cos(psi,-math.sin(psi),0), (math.sin(psi),math.cos(psi),0), (0,0,1)])
max_fwd = 250   # Max forward thrust
max_rev = 100   # Max reverse thrust
# Initialize position, velocity, acceleration vectors
x_map = np.zeros(3,1)
v_map = np.zeros(3,1)
a_map = np.zeros(3,1)


################################################################################
# SUBSCRIBERS
################################################################################
def runSubscribers():
    rospy.Subscriber("odometry/filtered", Odometry, odomFiltCallback)
    rospy.Subscriber("accel/filtered", AccelWithCovarianceStamped, accelFiltCallback)
    rospy.Subscriber("wamv/left_thrust_cmd", Float32, leftThrustCallback)
    rospy.Subscriber("wamv/right_thrust_cmd", Float32, rightThrustCallback)

def odomFiltCallback(data):
    x_map[0,0] = data.pose.pose[0]
    x_map[1,0] = data.pose.pose[1]
    x_map[2,0] = data.pose.pose[5]
    v_map[0,0] = data.twist.twist[0]
    v_map[1,0] = data.twist.twist[1]
    v_map[2,0] = data.twist.twist[5]
    psi = data.pose.pose[5]
    R_psi = np.array([(math.cos(psi,-math.sin(psi),0), (math.sin(psi),math.cos(psi),0), (0,0,1)])

def accelFiltCallback(data):
    return data.accel.accel

def leftThrustCallback(data):
    return data.thrust???

def rightThrustCallback(data):
    return data.thrust???

################################################################################
# MATH MODEL
################################################################################

a_map = np.transpose(np.array([accel[0], accel[1], accel[5]]))

x_parallel = np.transpose(R_psi)@x_map
v_parallel = np.transpose(R_psi)@v_map
a_parallel = np.transpose(R_psi)@a_map

u[0,0] = leftThrustCmd.subscribe()
u[0,1] = rightThrustCmd.subscribe()

# Mass matrix from Fossen Eq(7.95)
M = np.array([(mass-Xudot,0,0), (0,mass-Yvdot,m*xg-Yrdot), (0,m*xg-Yrdot, Iz-Nrdot)])

# Damping matrix from Fossen Eq(7.125)
D = np.array([(-Xu,0,0), (0,-Yv,-Yr), (0,-Nv,-Nr)])

# Total forces acting on WAMV
forces = M@a_parallel + D@v_parallel + tau_wind + tau_wave + np.transpose(R_psi)@b + tau_control
a_p = a_p + F./mass
v_p = v_p + a_p*dt
x_p = x_p + v_p*dt

# DO I NEED TO PUT THINGS IN A LOOP - WILL THE MATH MODEL RUN ONCE, THEN EXIT? PUT TRANSFORMATIONS IN THE CALLBACK?
# PUT SUBSCRIBERS IN MAIN?
# TO DO: THRUSTER CONFIG, MAKE TAU_CONTROL
# FINISH FINDING CURRENT POSITION
# MAKE PID FOR VRX
# MAKE GUIDANCE SECTION BY WEEKEND
