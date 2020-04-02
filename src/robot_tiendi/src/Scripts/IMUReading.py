import time
import RPi.GPIO as GPIO
import FaBo9Axis_MPU9250
import sys


import math
#from nav_msgs.msg import Odometry
#from geometry_msgs.msg import PoseWithCovarianceStamped
#from tf.transformations import euler_from_quaternion
#from geometry_msgs.msg import Point, Twist



class IMUReading():
    def __init__(self):
        # Creates a node with name 'speed_controller' and make sure it is a
        # unique node (using anonymous=True).
        #       rospy.init_node("move_motors", anonymous=True)
        # Publisher which will publish to the topic '/cmd_vel'.
        self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()


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
    try:
        while(True):
            print(imu.accel())
    except KeyboardInterrupt:
        pass


