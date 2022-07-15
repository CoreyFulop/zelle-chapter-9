# rballmatch.py

from random import random

def printIntro():
    print("This program simulates a match of raquetball between two")
    print("players called 'A' and 'B'. The abilities of each player is")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A has the")
    print("first serve in odd games of the match.\n")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate in the match? "))
    return a, b, n

def simNMatch(n, probA, probB):
    # Simulates a match of n games of raquetball between players
    # whose abilities are represented by the probabililty of winning a serve.
    # Returns number of game wins for A and B

    winsA = winsB = 0

    for i in range(1, n + 1):
        if (i%2 == 0):
            servFirst = "B" # B serves first in even games
        else:
            servFirst = "A" # A serves first in odd games

        scoreA, scoreB = simOneGame(probA, probB, servFirst)

        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1

    return winsA, winsB
 
def simOneGame(probA, probB, servFirst):
    # Simulates a single game or raquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    scoreA = 0
    scoreB = 0

    serving = servFirst

    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"

    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a raquetball game.
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames in match simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    if (winsA > winsB):
        print("A wins the match.")
    elif (winsB > winsA):
        print("B wins the match.")
    else: # winsA == winsB
        print("Match tied.")

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNMatch(n, probA, probB)
    printSummary(winsA, winsB)

if __name__ == "__main__":
    main()
