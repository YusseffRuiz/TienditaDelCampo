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

SPEEDL = 180
SPEEDR = SPEEDL


class MoveMotors():

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
            if(value == 0):
                self.MotorLeftSpeed.ChangeDutyCycle(0)
            for i in range(value):
                self.MotorLeftSpeed.ChangeDutyCycle(i)
        elif(direction == 'R'):
            if (value == 0):
                self.MotorRightSpeed.ChangeDutyCycle(0)
            for i in range(value):
                self.MotorRightSpeed.ChangeDutyCycle(i)


    def setSpeed(self, speed):
        if(speed == 0):
            self.MotorLeftSpeed.ChangeDutyCycle(0)
            self.MotorRightSpeed.ChangeDutyCycle(0)
        else:
            for i in range(speed):
                self.MotorLeftSpeed.ChangeDutyCycle(i)
                self.MotorRightSpeed.ChangeDutyCycle(i)

    def initializeFront(self):
        GPIO.output(self.RightMotorP, GPIO.HIGH)
        GPIO.output(self.RightMotorN, GPIO.LOW)
        GPIO.output(self.LeftMotorP, GPIO.HIGH)
        GPIO.output(self.LeftMotorN, GPIO.LOW)
        # print("Moving Forward")

    def initializeBack(self):
        GPIO.output(self.RightMotorN, GPIO.HIGH)
        GPIO.output(self.RightMotorP, GPIO.LOW)
        GPIO.output(self.LeftMotorN, GPIO.HIGH)
        GPIO.output(self.LeftMotorP, GPIO.LOW)
        # print("Moving Backwards")

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

    def pControl(self):
        print("Proportional Control")

    def integralControl(self):
        print("Integral Control")

    def derivativeControl(self):
        print("DerivativeControl")

    def robotMovement(self, direction):

        self.initializeFront()
        # counter = 1
        self.idleMotors()
        if direction == b'q':
            self.stopMotors()
            # counter = 3
            print("Quit")
        elif (direction == b'w'):
            # if (counter == 1):
            self.initializeFront()
                # counter += 1
            print("Front")
            self.moveStraight(SPEEDL)
        elif (direction == b'x'):
            # if (counter == 1):
            self.initializeBack()
                # counter += 1
            print("Back")
            self.moveStraight(SPEEDL)
        elif (direction == b'a'):
            self.turnLeft(SPEEDL)
            # counter = 3
            print("Left")
        elif (direction == 'd'):
            self.turnRight(SPEEDL)
            # counter = 3
            print("Right")
        elif (direction == 's'):
            self.idleMotors
            # counter = 3
            print("Stop")




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
