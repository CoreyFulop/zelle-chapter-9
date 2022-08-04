# monte_carlo_pi.py

import random

from graphics import *

def printIntro():
    print("This program determines an approximation to pi using a Monte Carlo technique.\n")

def getInput():
    n = eval(input("Enter the number of darts to throw: "))
    return n

def simNThrows(n):
    h = 0
    win = drawDartBoard()
    for i in range(n):
        x, y, = getCoords()
        drawPoint(x, y, win)
        if x**2 + y**2 <= 1:
            h += 1
    return h, win

def drawDartBoard():
    win = GraphWin("Dart Board", 400, 400)
    win.setCoords(-1.0, -1.0 , 1.0 , 1.0)
    centre = Point(0, 0)
    board = Circle(centre, 1)
    board.setFill("cyan")
    board.setOutline("cyan")
    board.draw(win)
    return win

def drawPoint(x, y, win):
    point = Point(x, y)
    point.setFill("red")
    point.draw(win)
    
def getCoords():
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    return x, y

def printSummary(h, n):
    print(f"\nWith {h} hits from {n} darts thrown, the approximation to pi is:")
    print(f"{4 * (h/n)}.")

def closeWin(win):
    exitMess = Text(Point(0,0), "Click to close")
    exitMess.draw(win)
    win.getMouse()
    win.close()

def main():
    printIntro()
    n = getInput()
    h, win = simNThrows(n)
    printSummary(h, n)
    closeWin(win)

if __name__ == "__main__":
    main()

