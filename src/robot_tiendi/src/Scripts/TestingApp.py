import sys
import time
import math
# import keyboard
import curses

##source: https://www.thepythoncode.com/article/control-keyboard-python
from MoveMotors import MoveMotors

speed = 60
counter = 1

if __name__ == "__main__":
    robot = MoveMotors()
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    try:
        robot.initializeFront()
        while(True):
            counter = 1
            char = screen.getch()
            robot.idleMotors()
            while(curses.KEY_UP):
            # while(keyboard.is_pressed('up')):
                if(counter==1):
                    robot.initializeFront()
                    counter+=1
                robot.moveStraight(speed)
                print("Front")
            while(curses.KEY_DOWN):
            # while(keyboard.is_pressed('down')):
                if(counter == 1):
                    robot.initializeBack()
                    counter+=1
                robot.moveStraight(speed)
                print("Back")
            while(curses.KEY_LEFT):
            # while(keyboard.is_pressed('left')):
                robot.turnLeft(speed)
                print("Left")
            while(curses.KEY_RIGHT):
            # while(keyboard.is_pressed('right')):
                robot.turnRight(speed)
                print("Right")

    except KeyboardInterrupt:
        print("Ending Program")
        pass