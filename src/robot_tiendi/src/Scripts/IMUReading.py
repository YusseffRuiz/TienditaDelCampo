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
    try:
        while(True):
            prevTime = currentTime
            currentTime = time.time()
            elapsedTime = currentTime - prevTime
            acX, acY, acZ = imu.accel()
            gyX, gyY, gyZ = imu.gyro()
            accAngleX = math.atan((acY / 16384) / math.sqrt(pow((acX / 16384), 2) + pow((acZ/16384), 2))) * imu.radToDeg
            accAngleY = math.atan((acX / 16384) / math.sqrt(pow((acY / 16384), 2) + pow((acZ / 16384), 2))) * imu.radToDeg

            gyroX = gyX/131
            gyroY = gyY/131
            gyroZ = gyZ/131

            roll = 0.98 * (angleX + gyroX * elapsedTime) + 0.02 * accAngleX
            pitch = 0.98 * (angleY + gyroY * elapsedTime) + 0.02 * accAngleY

            error = angleY - desiredAngle
            print("AcceX: " + accAngleX)
            print("AcceY: " + accAngleY)
            print("RawAcZ " + acZ)

            print("GyroX: " + gyroX)
            print("GyroY: " + gyroY)
            print("GyroZ: " + gyroZ)

            print("Roll: " + roll)
            print("Pitch " + pitch)

            time.sleep(1)




    except KeyboardInterrupt:
        pass


