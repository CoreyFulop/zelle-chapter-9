# vball_rallyscoring.py

from random import random

def printIntro():
    print("This program simulates a game of volleyball")
    print("(with rally scoring) between teams 'A' and 'B'.")
    print("The abilities of each team are indicated by a probability (a")
    print("number between 0 and 1) that the team will")
    print("win a point when serving. The game starts with")
    print("team A serving.\n")

def getInputs():
    probA = eval(input("What is the prob. team A wins a serve? "))
    probB = eval(input("What is the prob. team B wins a serve? "))
    return probA, probB

def simGame(probA, probB):
    pointsA = pointsB = 0
    server = "A"
    while not endGame(pointsA, pointsB):
        if server == "A":
            if random() < probA:
                pointsA += 1
            else:
                pointsB += 1
                server = "B"
        else:
            if random() < probB:
                pointsB += 1
            else:
                pointsA += 1
                server = "A"
    return pointsA, pointsB

def endGame(pointsA, pointsB):
    return (pointsA >= 25 and pointsA >= pointsB + 2) or (pointsB >= 25 and pointsB >= pointsA + 2)

def results(pointsA, pointsB):
    if pointsA > pointsB:
        print(f"Team A wins, {pointsA} to {pointsB}.")
    else:
        print(f"Team B wins, {pointsB} to {pointsA}.")

def main():
    printIntro()
    probA, probB = getInputs()
    pointsA, pointsB = simGame(probA, probB)
    results(pointsA, pointsB)

if __name__ == "__main__":
    main()
