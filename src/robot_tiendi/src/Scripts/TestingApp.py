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
            if char == ord('q'):
                break
            elif(char == curses.KEY_UP):
            # while(keyboard.is_pressed('up')):
                if(counter==1):
                    robot.initializeFront()
                    counter+=1
                robot.moveStraight(speed)
                print("Front")
            elif(char == curses.KEY_DOWN):
            # while(keyboard.is_pressed('down')):
                if(counter == 1):
                    robot.initializeBack()
                    counter+=1
                robot.moveStraight(speed)
                print("Back")
            elif(char == curses.KEY_LEFT):
            # while(keyboard.is_pressed('left')):
                robot.turnLeft(speed)
                print("Left")
            elif(char == curses.KEY_RIGHT):
            # while(keyboard.is_pressed('right')):
                robot.turnRight(speed)
                print("Right")
            elif(char == 10):
                robot.idleMotors


    except KeyboardInterrupt:
        pass
    finally:
        print("Ending Program")
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()