import rospy
import sys
import time
import RPi.GPIO as GPIO

import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist



class ReadIMU:

    def __init__(self):
        self.ax = 0

    def accelerometerAngles(self, x, y, z):
        angleX = atan2(x/(x*x+y*y))
        angleY = atan2(y/(x*x+z*z))
        return angleX, angleY


    def printing(self):
        print ("Hello World")

    if __name__ == "__main__":
        try:
            x = ReadIMU()


        except rospy.ROSInterruptException:
            x.stopMotors()
            pass