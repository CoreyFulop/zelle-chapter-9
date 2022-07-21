# vball_compare.py

from random import random

def printIntro():
    print("This program compares the outcome of volleyball games played between")
    print("team 'A' and 'B', using either regular or rally scoring.")
    print("\nThe ability of team A and team B is indicated by a probability")
    print("(between 0 and 1) that the team will win a point when serving.")
    print("\nTeam A always has the first serve in each game.\n")

def getInputs():
    probA = eval(input("What is the prob. team A wins on a serve? "))
    probB = eval(input("What is the prob. team B wins on a serve? "))
    n = eval(input("How many games to simulate? "))
    return probA, probB, n

def simulateNGamesNormal(probA, probB, n):
    winsA_n = winsB_n = 0
    for i in range(n):
        winner = simOneNormalGame(probA, probB)
        if winner == "A":
            winsA_n += 1
        else: # winner is B
            winsB_n += 1
    return winsA_n, winsB_n    

def simulateNGamesRally(probA, probB, n):
    winsA_r = winsB_r = 0
    for i in range(n):
        winner = simOneRallyGame(probA, probB)
        if winner == "A":
            winsA_r += 1
        else: # winner is B
            winsB_r += 1
    return winsA_r, winsB_r

def simOneNormalGame(probA, probB):
    scoreA = scoreB = 0
    server = "A"
    while not gameOverNormal(scoreA, scoreB):
        if server == "A":
            if random() < probA:
                scoreA += 1
            else:
                server = "B"
        else: # server is B
            if random() < probB:
                scoreB += 1
            else:
                server = "A"
    if scoreA > scoreB:
        winner = "A"
    else:
        winner = "B"
    return winner

def gameOverNormal(scoreA, scoreB):
    return (scoreA >= 15 and scoreA >= scoreB + 2) or (scoreB >= 15 and scoreB >= scoreA + 2)

def simOneRallyGame(probA, probB):
    scoreA = scoreB = 0
    server = "A"
    while not gameOverRally(scoreA, scoreB):
        if server == "A":
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
                server = "B"
        else: # server is B
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
                server = "A"
    if scoreA > scoreB:
        winner = "A"
    else:
        winner = "B"
    return winner

def gameOverRally(scoreA, scoreB):
    return (scoreA >= 25 and scoreA >= scoreB + 2) or (scoreB >= 25 and scoreB >= scoreA +2)

def printSummary(winsA_n, winsB_n, winsA_r, winsB_r, n):
    print()
    print(f"Team A - Normal wins: {winsA_n} ({winsA_n/n * 100:.2f}%)")
    print(f"Team A - Rally wins: {winsA_r} ({winsA_r/n * 100:.2f}%)")
    print(f"Team B - Normal wins: {winsB_n} ({winsB_n/n * 100:.2f}%)")
    print(f"Team B - Rally wins: {winsB_r} ({winsB_r/n * 100:.2f}%)")
    
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA_n, winsB_n = simulateNGamesNormal(probA, probB, n)
    winsA_r, winsB_r = simulateNGamesRally(probA, probB, n)
    printSummary(winsA_n, winsB_n, winsA_r, winsB_r, n)

if __name__ == "__main__":
    main()
