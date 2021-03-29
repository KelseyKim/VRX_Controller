#! /usr/bin/env python2

"""Subscribe to current yaw orientation /psiMap
 Subscribe to map frame pose to be transformed
 Convert to vessel parallel coordinates
 Publish to /poseParallel
 Published topics will be used by PID package to create control commands"""

import rospy
import math

from std_msgs.msg import Float64
from nav_msgs.msg import Odometry

psiMap = 0

# Subscribers
def createSubscribers():
    # Subscribe to pose in map frame to be transformed into vessel parallel
    rospy.Subscriber("/poseMap", Odometry, poseMapCallback, queue_size=10)
    # Subscribe to psi angle between map frame and vessel parallel
    rospy.Subscriber("/psiMap", Float64, psiMapCallback, queue_size=10)

# Callback function for /poseMap subscriber
def poseMapCallback(data):
    poseParallel = mapToParallel(data, psiMap)
    # Publish pose in vessel parallel coordinates to /poseParallel
    posePub = rospy.Publisher("/poseParallel", Odometry, queue_size=10)
    posePub.publish(poseParallel)
    rate = rospy.Rate(10)

def psiMapCallback(data):
    psiMap = data

# Convert coordinates from map frame to vessel parallel
def mapToParallel(poseMap, psiMap):
    poseParallel = Odometry()
    xMap = poseMap.pose.pose.position.x
    yMap = poseMap.pose.pose.position.y
    # Yaw rotation of psi about z-axis
    xParallel = math.cos(psiMap)*xMap - math.sin(psiMap)*yMap
    yParallel = math.sin(psiMap)*xMap + math.cos(psiMap)*yMap
    # map frame has positive z-axis upwards --> pi rotation about x-axis to coincide with vp positive z-axis downwards
    xParallel = 1*xParallel
    yParallel = math.cos(math.pi)
    # Put pose in Odometry message format
    poseParallel.pose.pose.position.x = xParallel
    poseParallel.pose.pose.position.y = yParallel
    return poseParallel

if __name__ == "__main__":
    rospy.init_node("map_to_parallel_node")
    while not rospy.is_shutdown():
        createSubscribers()
