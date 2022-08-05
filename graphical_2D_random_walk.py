# graphical_2D_random_walk.py

import random

import math

from graphics import *

def printIntro():
    print("This program traces a random walk in 2D.\n")

def getInput():
    n = eval(input("How many steps are there in the random walk: "))
    return n

def drawRandomWalk(n):
    win = GraphWin("Random Walk", 500, 500)
    win.setCoords(-50.0, -50.0, 50.0, 50.0)
    x = y = 0.0
    for i in range(n):
        angle = random.random() * 2 * math.pi
        new_x = x + math.cos(angle)
        new_y = y + math.sin(angle)
        line = Line(Point(x, y), Point(new_x, new_y))
        line.draw(win)
        x, y = new_x, new_y
    endMessage = Text(Point(0, 45), "Click to exit")
    endMessage.draw(win)
    win.getMouse()
    win.close()
        
def main():
    printIntro()
    n = getInput()
    drawRandomWalk(n)
    
if __name__ == "__main__":
    main()
