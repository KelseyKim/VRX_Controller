#! /usr/bin/env python2

import rospy
import actionlib

from controller.msg import navigateToCoordsAction, navigateToCoordsFeedback, navigateToCoordsResult, navigateToCoordsGoal
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float64

def feedbackCallback(feedback):
    # Need to convert distancToGoal to meters
    print("Distance to goal: " + str(feedback.distanceToGoal))
    print ("Current coordinates: " + str(feedback.currentCoords))

# Actual function to process incoming desired coordinates
def navigationClient(desiredCoords):
    # Create action client (inputs are actionName, actionMessage)
    client = actionlib.SimpleActionClient("navigateToCoords_action", navigateToCoordsAction)

    client.wait_for_server()
    # Put desired coordinates from desiredCoords list into NavSatFix message
    desiredCoords_NavSatFix = NavSatFix()
    desiredCoords_NavSatFix.latitude = desiredCoords[0]
    desiredCoords_NavSatFix.longitude = desiredCoords[1]
    desiredCoords_NavSatFix.altitude = desiredCoords[2])
    # Send desired coordinates to action server
    goal = navigateToCoordsGoal(desiredCoords_NavSatFix)
    client.send_goal(goal,feedback_cb = feedbackCallback)

    client.wait_for_result()
    return client.get_result()

if __name__ == "__main__":
    try:
        rospy.init_node("navigateToCoords_action_client_node")
        # Ask user for desired coordinates
        desiredLat = input("Enter desired latitude: ")
        desiredLon = input("Enter desired longitude: ")
        desiredAlt = 0

        desiredCoords = [float(desireLat), float(desiredLon), float(desiredAlt)]
        # Result from action server
        result = navigationClient(desiredCoords)
        print(result)


    except rospy.ROSInterruptException:
        print("Program interrupted")
