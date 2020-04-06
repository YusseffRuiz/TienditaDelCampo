import time
import RPi.GPIO as GPIO
import FaBo9Axis_MPU9250
import sys


import math
#from nav_msgs.msg import Odometry
#from geometry_msgs.msg import PoseWithCovarianceStamped
#from tf.transformations import euler_from_quaternion
#from geometry_msgs.msg import Point, Twist
##http://www.electronoobs.com/eng_robotica_tut6_2.php


class IMUReading():
    def __init__(self):
        # Creates a node with name 'speed_controller' and make sure it is a
        # unique node (using anonymous=True).
        #       rospy.init_node("move_motors", anonymous=True)
        # Publisher which will publish to the topic '/cmd_vel'.
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        self.radToDeg = 180/3.141592654


    def calibrate(self):
        ##do something
        print("Something")

    def accel(self):
        accel = self.mpu9250.readAccel()
        return accel['x'], accel['y'], accel['z']


    def gyro(self):
        gyro = self.mpu9250.readGyro()
        return gyro['x'], gyro['y'], gyro['z']

    def mag(self):
        mag = self.mpu9250.readMagnet()
        return mag['x'], mag['y'], mag['z']



if __name__ == "__main__":
    imu = IMUReading()
    angleX = 0
    angleY = 0
    currentTime = time.time()
    desiredAngle = 0
    counter = 0
    acX = 0
    acY = 0
    acZ = 0
    gyX = 0
    gyY = 0
    gyZ = 0

    raw_acX, raw_acY, raw_acZ = imu.accel()
    raw_gyX, raw_gyY, raw_gyZ = imu.gyro()

    try:
        while(True):
            prevTime = currentTime
            currentTime = time.time()
            elapsedTime = currentTime - prevTime
            prev_rawacX, prev_rawacY, prev_rawacZ = raw_acX, raw_acY, raw_acZ
            prev_rawgyX, prev_rawgyY, prev_rawgyZ = raw_gyX, raw_gyY, raw_gyZ

            raw_acX, raw_acY, raw_acZ = imu.accel()
            raw_gyX, raw_gyY, raw_gyZ = imu.gyro()


            if (counter <= 10):
                counter += 1
                time.sleep(0.3)
                if(counter == 10):
                    base_acX = raw_acX
                    base_acY = raw_acY
                    base_acZ = raw_acZ

                    base_gyX = raw_gyX
                    base_gyY = raw_gyY
                    base_gyZ = raw_gyZ
                    print("Calibrated")


            else:
                acX = acY = acZ = gyX = gyY = 0.001
                if(abs(raw_acX - prev_rawacX) > 0.1):
                    acX = raw_acX - base_acX
                elif(abs(raw_acY - prev_rawacY) > 0.1):
                    acY = raw_acY - base_acY
                elif(abs(raw_acZ - prev_rawacZ) > 0.1):
                    acZ = raw_acZ - base_acZ

                if (abs(raw_gyX - prev_rawgyX) > 0.1):
                    gyX = raw_gyX - base_gyX
                elif (abs(raw_gyY - prev_rawgyY) > 0.1):
                    gyY = raw_gyY - base_gyY
                elif (abs(raw_gyZ - prev_rawgyZ) > 0.1):
                    gyZ = raw_gyZ - base_gyZ



                accAngleX = math.atan((acY / 16384) / math.sqrt(pow((acX / 16384), 2) + pow((acZ/16384), 2))) * imu.radToDeg
                accAngleY = math.atan((acX / 16384) / math.sqrt(pow((acY / 16384), 2) + pow((acZ / 16384), 2))) * imu.radToDeg

                gyroX = gyX/131
                gyroY = gyY/131
                gyroZ = gyZ/131

                roll = 0.98 * (angleX + gyroX * elapsedTime) + 0.02 * accAngleX
                pitch = 0.98 * (angleY + gyroY * elapsedTime) + 0.02 * accAngleY

                error = angleY - desiredAngle
                print("AcceX: " + str(acX) + " | " + "GyroX: " + str(gyroX) + " | " + "Roll: " + str(roll))
                print("AcceY: " + str(acY) + " | " + "GyroY: " + str(gyroY) + " | " + "Pitch " + str(pitch))
                print("RawAcZ " + str(acZ) + " | " + "GyroZ: " + str(gyroZ))

                print(" ")






    except KeyboardInterrupt:
        pass


