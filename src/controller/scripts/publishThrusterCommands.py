#!/usr/bin/env python2

import rospy
import numpy as np
import math

from std_msgs.msg import Float64
from nav_msgs.msg import Odometry

XForce = 0
NTorque = 0
xSetpoint = 0
yawSetpoint = 0

# Subscribe to control_effort force and torque topics
def createSubscribers(XForce, NTorque):
    rospy.Subscriber("/X/control_effort", Float64, XCallback, queue_size=10)
    rospy.Subscriber("/N/control_effort", Float64, NCallback, queue_size=10)
    rospy.Subscriber("/xPosSetpoint", Float64, xSetpointCallback, queue_size=10)
    rospy.Subscriber("/yawAttSetpoint", Float64, yawSetpointCallback, queue_size=10)

def XCallback(data):
    XForce = data

def NCallback(data):
    NTorque = data

def xSetpointCallback(data):
    xSetpoint = data

def yawSetpoint(data):
    yawSetpoint = data

def calculateThrusterCmds(XControlEffort, NControlEffort, yp):
    # Thruster configuration matrix from Fossen
    b = np.array([(1,1), (0,0), (yp,-yp)])
    # Vertical force/torque vector
    tau = np.array([(XControlEffort), (0), (NControlEffort)])
    # Find thrust commands tau = b*u ---> u = b^-1 * tau
    u = np.linalg.inv(b)@tau

    for thrust in u:
        if thrust < 0:
            thrust = thrust/100
        else:
            thrust = thrust/250

    return u

def publishThrusts(thrustVec):
    rospy.Publisher("/wamv/left_thrust_cmd", thrustVec[0][0], queue_size=10)
    rospy.Publisher("/wamv/right_thrust_cmd", thrustVec[1][0], queue_size=10)

if __name__=='__main__':
    rospy.init_node("publish_thruster_cmds_node", anonymous=True)
    yp = 1.027135
    leftThrustCmd = 0
    rightThrustCmd = 0
    u = np.array([[0][0]])

    while not rospy.is_shutdown():
        createSubscribers()
        # Do turning first
        if abs(yawSetpoint) > 10*math.pi/180:   # If yaw is off by 10 degrees
            u = calculateThrusterCmds(0, NTorque, yp)
        elif abs(xSetpoint) < 10:
            u = numpy.array([(0), (0)])
        else:
            u = calculateThrusterCmds(XForce, 0, yp)

        publishThrusts(u)
