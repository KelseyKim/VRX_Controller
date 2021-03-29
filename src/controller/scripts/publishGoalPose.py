#! /usr/bin/env python2

import rospy
import math

from nav_msgs.msg import Odometry
from std_msgs.msg import Float64

desiredOdom = Odometry()
currentOdom = Odometry()

def createSubscribers():
    rospy.Subscriber("/desired/poseParallel", Odometry, desiredCallback)
    rospy.Subscriber("/current/poseParallel", Odometry, currentCallback)

def desiredCallback(data):
    desiredOdom = data

def currentCallback(data):
    currentOdom = data

def calculateDifferences(desiredOdometry, currentOdometry):
    xDiff = desiredOdometry.pose.pose.position.x - currentOdometry.pose.pose.position.x
    yDiff = desiredOdometry.pose.pose.position.y - currentOdometry.pose.pose.position.y
    yawDiff = math.asin(yDiff/xDiff)
    distanceDiff = math.squrt(xDiff**2 + yDiff**2)
    return [distanceDiff, yawDiff]

if __name__ == "__main__":
    rospy.init_node("publish_goal_pose")
    xPub = rospy.Publisher("/x", Float64, queue=10)
    yawPub = rospy.Publisher("/psi", Float64, queue=10)
    while not rospy.is_shutdown():
        createSubscirbers()
        distance, yaw = calculateDifferences(desiredOdom, currentOdom)
        xPub.publish(distance)
        yawPub.publish(yaw)
