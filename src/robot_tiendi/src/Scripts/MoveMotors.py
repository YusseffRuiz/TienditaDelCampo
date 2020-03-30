#! /usr/bin/env python

import rospy
import sys
import time
import RPi.GPIO as GPIO

import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist



class MoveMotors:

    def __init__(self):

        # Creates a node with name 'speed_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node("move_motors", anonymous=True)
        # Publisher which will publish to the topic '/cmd_vel'.
        self.mode = GPIO.getmode()
        GPIO.cleanup()
        self.LeftMotorP = 26
        self.pwmL = 13
        self.LeftMotorN = 19
        self.RightMotorP = 20
        self.pwmR = 21
        self.RightMotorN = 16
        self.r = rospy.Rate(4)



        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RightMotorF, GPIO.OUT)
        GPIO.setup(self.RightMotorB, GPIO.OUT)
        GPIO.setup(self.LeftMotorF, GPIO.OUT)
        GPIO.setup(self.LeftMotorB, GPIO.OUT)
        GPIO.setup(self.pwmL, GPIO.OUT)
        GPIO.setup(self.pwmR, GPIO.OUT)

        self.MotorLeftSpeed = GPIO.PWM =(self.pwmL, 100)
        self.MotorRightSpeed = GPIO.PWM = (self.pwmR, 100)
        self.MotorLeftSpeed.start()
        self.MotorRightSpeed.start()
        rospy.loginfo("GPIOs cleaned and assigned")

    def set(self, direction, value):
        if(direction == 'L'):
            self.MotorLeftSpeed.ChangeDutyCycle(value)
        elif(direction == 'R'):
            self.MotorRightSpeed.ChangeDutyCycle(value)



    def forward(self):
        GPIO.output(self.RightMotorP, GPIO.HIGH)
        GPIO.output(self.RightMotorN, GPIO.LOW)
        GPIO.output(self.LeftMotorP, GPIO.HIGH)
        GPIO.output(self.LeftMotorN, GPIO.LOW)
        print("Moving Forward")
        self.r.sleep()

    def reverse(self):
        GPIO.output(self.RightMotorN, GPIO.HIGH)
        GPIO.output(self.RightMotorP, GPIO.LOW)
        GPIO.output(self.LeftMotorN, GPIO.HIGH)
        GPIO.output(self.LeftMotorP, GPIO.LOW)
        print("Moving Backwards")
        self.r.sleep()

    def stopMotors(self):
        self.MotorRightSpeed.stop()
        self.MotorLeftSpeed.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    try:
        x = MoveMotors()
        x.forward()
        x.stopMotors()
    except rospy.ROSInterruptException:
        pass