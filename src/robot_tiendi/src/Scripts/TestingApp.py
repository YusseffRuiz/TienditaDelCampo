import sys
import time
import math
import keyboard

##source: https://www.thepythoncode.com/article/control-keyboard-python
from src.robot_tiendi.src.Scripts.MoveMotors import MoveMotors

speed = 60
counter = 1

if __name__ == "__main__":
    # robot = MoveMotors()
    try:
        robot.initializeFront()
        while(True):
            counter = 1
            robot.idleMotors()
            while(keyboard.is_pressed('up')):
                if(counter==1):
                    robot.initializeFront()
                    counter+=1
                robot.moveStraight(speed)
                print("Front")
            while(keyboard.is_pressed('down')):
                if(counter == 1):
                    robot.initializeBack()
                    counter+=1
                robot.moveStraight(speed)
                print("Back")
            while(keyboard.is_pressed('left')):
                robot.turnLeft(speed)
                print("Left")
            while(keyboard.is_pressed('right')):
                robot.turnRight(speed)
                print("Right")

    except KeyboardInterrupt:
        print("Ending Program")
        pass