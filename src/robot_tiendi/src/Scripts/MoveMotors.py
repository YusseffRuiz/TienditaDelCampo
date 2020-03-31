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
        self.LeftMotorN = 26
        self.pwmL = 13
        self.LeftMotorP = 19
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
        self.MotorLeftSpeed.start(0)
        self.MotorRightSpeed.start(0)
  #      rospy.loginfo("GPIOs cleaned and assigned")

    def set(self, direction, value):
        if(direction == 'L'):
            self.MotorLeftSpeed.ChangeDutyCycle(value)
        elif(direction == 'R'):
            self.MotorRightSpeed.ChangeDutyCycle(value)

    def setSpeed(self, speed):
        self.set('L', speed)
        self.set('R', speed)

    def initializeFront(self):
        GPIO.output(self.RightMotorP, GPIO.HIGH)
        GPIO.output(self.RightMotorN, GPIO.LOW)
        GPIO.output(self.LeftMotorP, GPIO.HIGH)
        GPIO.output(self.LeftMotorN, GPIO.LOW)
        print("Moving Forward")

    def initializeBack(self):
        GPIO.output(self.RightMotorN, GPIO.HIGH)
        GPIO.output(self.RightMotorP, GPIO.LOW)
        GPIO.output(self.LeftMotorN, GPIO.HIGH)
        GPIO.output(self.LeftMotorP, GPIO.LOW)
        print("Moving Backwards")

    def moveStraight(self, speed):
        self.setSpeed(speed)


    def turnRight(self, speed):
        self.set('L', speed)
        self.set('R', 0)

    def turnLeft(self, speed):
        self.set('R', speed)
        self.set('L', 0)

    def diag(self, direction, speed):
        if(direction == 'R'):
            self.set('R', speed-10)
        elif(direction == 'L'):
            self.set('L', speed - 10)

    def idleMotors(self):
        self.initializeFront()
        self.setSpeed(0)


    def stopMotors(self):
        self.initializeFront()
        self.MotorRightSpeed.stop()
        self.MotorLeftSpeed.stop()
        GPIO.cleanup()
        print("Stopping Motors")


if __name__ == "__main__":
    x = MoveMotors()
    try:
        x.initializeFront()

        print("First movement, move front")
        x.moveStraight(60)
        time.sleep(3)

        x.idleMotors()
        time.sleep(1)

        print("Move Back")
        x.initializeBack()
        x.moveStraight(60)

        time.sleep(3)
        x.idleMotors()
        time.sleep(1)

        print("Turn Right")
        x.turnRight(60)

        time.sleep(2)

        x.idleMotors()

        time.sleep(1)

        print("Turn Left")
        x.turnLeft(60)

        time.sleep(2)

        x.idleMotors()

        time.sleep(1)

        print("diagonal Movement")
        x.moveStraight(60)
        x.diag('R', 60)

        time.sleep(2)

        x.idleMotors()

        x.stopMotors()

        print("Done")


    except KeyboardInterrupt:
        x.stopMotors()
        pass
#    except rospy.ROSInterruptException:
#        pass
