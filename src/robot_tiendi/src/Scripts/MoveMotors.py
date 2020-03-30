#! /usr/bin/env python

#import rospy
import sys
import time
import RPi.GPIO as GPIO

import math
#from nav_msgs.msg import Odometry
#from geometry_msgs.msg import PoseWithCovarianceStamped
#from tf.transformations import euler_from_quaternion
#from geometry_msgs.msg import Point, Twist



class MoveMotors:

    def __init__(self):

        # Creates a node with name 'speed_controller' and make sure it is a
        # unique node (using anonymous=True).
 #       rospy.init_node("move_motors", anonymous=True)
        # Publisher which will publish to the topic '/cmd_vel'.
        self.mode = GPIO.getmode()
        self.LeftMotorP = 26
        self.pwmL = 13
        self.LeftMotorN = 19
        self.RightMotorP = 20
        self.pwmR = 21
        self.RightMotorN = 16
#        self.r = rospy.Rate(4)



        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RightMotorP, GPIO.OUT)
        GPIO.setup(self.RightMotorN, GPIO.OUT)
        GPIO.setup(self.LeftMotorP, GPIO.OUT)
        GPIO.setup(self.LeftMotorN, GPIO.OUT)
        GPIO.setup(self.pwmL, GPIO.OUT)
        GPIO.setup(self.pwmR, GPIO.OUT)

        self.MotorLeftSpeed = GPIO.PWM(self.pwmL, 100)
        self.MotorRightSpeed = GPIO.PWM(self.pwmR, 100)
        self.MotorLeftSpeed.start(1)
        self.MotorRightSpeed.start(1)
  #      rospy.loginfo("GPIOs cleaned and assigned")

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
#        self.r.sleep()

    def reverse(self):
        GPIO.output(self.RightMotorN, GPIO.HIGH)
        GPIO.output(self.RightMotorP, GPIO.LOW)
        GPIO.output(self.LeftMotorN, GPIO.HIGH)
        GPIO.output(self.LeftMotorP, GPIO.LOW)
        print("Moving Backwards")
 #       self.r.sleep()

    def stopMotors(self):
        self.MotorRightSpeed.stop()
        self.MotorLeftSpeed.stop()
        GPIO.cleanup()
	print("Stopping Motors")


if __name__ == "__main__":
    try:
	x = MoveMotors()
	x.forward()
	while(True):
           # x.forward()
            x.set('L', 50)
	    x.set('R', 50)
	#x.stopMotors()
    except KeyboardInterrupt:
	x.stopMotors()
	pass
#    except rospy.ROSInterruptException:
#        pass
