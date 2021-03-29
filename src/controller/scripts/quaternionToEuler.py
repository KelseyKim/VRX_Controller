#! /usr/bin/env python2

import rospy
import tf

from nav_msgs.msg import Odometry
from std_msgs.msg import Float64


def subscribeToQuaternions():
    rospy.Subscriber("/odometry/filtered_map", Odometry, publishEuler)

def publishEuler(data):
    # Convert orientation from Quaternions to Euler angles
    quaternion = (data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    yaw = euler[2]
    yawPub = rospy.Publisher("/psiMap", Float64, queue=10)
    yawPub.publish(yaw)



if __name__ =="__main__":
    rospy.init_node("quaternion_to_Euler_node")
    while not rospy.is_shutdown():
        subscribeToQuaternions()
