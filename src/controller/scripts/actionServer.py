#! /usr/bin/env python2

import rospy
import actionlib
import math

from controller.msg import navigateToCoordsAction, navigateToCoordsFeedback, navigateToCoordsResult
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float64


class navigateToCoordsClass:
    def __init__(self):
        # Create action server
        self.action_server = actionlib.SimpleActionServer("navigateToCoords_action", navigateToCoordsAction, self.navigateCallback)
        # Subscribe to current lat, lon, alt (filtered estimate from robot_localization in lat/lon)
        self.currentCoordsSub = rospy.Subscriber("/gps/filtered_map", NavSatFix, self.updateCurrentCoords)
        # Publisher to publish desired coordinates
        self.desiredCoordsPub = rospy.Publisher("/desiredCoordinatesLatLon", NavSatFix, queue=10)
        # Initialize current position in lat, lon
        self.currentCoords = None
        # Initialize goal position in lat, lon
        self.goalCoords = None
        # Define distance threshold to desired coordinates
        self.distanceThreshold = 0.00002    # Roughly 2.22m
        # Feedback publishing rate
        self.feedbackRate = rospy.Rate(1)

    def navigateCallback(self, goal):
        self.goalCoords = [goal.latitude, goal.longitude, goal.altitude]

        while self.currentCoords == None and not rospy.is_shutdown():
            print("Current coordinates not detected")
            rospy.sleep(5)

        print("Current coordinates detected")
        distanceToGo = math.dist(self.currentCoords, self.goalCoords)
        # While distance from current coordinates to goal coordinates > distance threshold (~2.22m)
        while distanceToGo > self.distanceThreshold:
            # Publish desired coordinates for latLonToParallel.py to subscribe to
            self.desiredCoordsPub.publish(goal)
            # Publish distance to go and current coordinates
            self.action_server.publish_feedback(navigateToCoordsFeedback(distanceToGoal=distanceToGo, currentCoords=self.currentCoords))
            # Publish every 1s
            self.feedback_rate.sleep()
            # Recalculate distance to go
            distanceToGo = math.dist(self.currentCoords, self.goalCoords)

        self.action_server.set_succeeded(navigateToCoords(finalCoords=self.currentCoords))


    def updateCurrentCoords(self, currentCoordinates):
        self.currentCoords = [currentCoordinates.latitude, currentCoordinates.longitude, currentCoordinates.altitude]


if __name__ == "__main__":
    rospy.init_node("navigateToCoords_action_server_node")
    server = navigateToCoordsClass()
    rospy.spin()
