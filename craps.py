# craps.py

import random

def printIntro():
    print("This program simulates n games of craps.\n")

def getInput():
    n_games = eval(input("How many games to simulate? "))
    return n_games

def simNGames(n_games):
    wins = losses = 0
    for i in range(n_games):
        outcome = simOneGame()
        if outcome == "win":
            wins += 1
        else:
            losses += 1
    return wins, losses

def simOneGame():
    die_1, die_2 = roll_die() 
    initial_roll = die_1 + die_2
    if initial_roll == 2 or initial_roll == 3 or initial_roll == 12:
        outcome = "loss"
    elif initial_roll == 7 or initial_roll == 11:
        outcome = "win"
    else:
        outcome = rollForPoint(initial_roll)
    return outcome

def roll_die():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    return die_1, die_2

def rollForPoint(initial_roll):
    end_loop = False
    while not end_loop:
        die_1, die_2 = roll_die()
        roll = die_1 + die_2
        if roll == 7:
            return "loss"
        if roll == initial_roll:
            return "win"

def printSummary(wins, losses, n_games):
    print()
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Probability of winning: {wins/n_games:.3f}")
    
def main():
    printIntro()
    n_games = getInput()
    wins, losses = simNGames(n_games)
    printSummary(wins, losses, n_games)

if __name__ == "__main__":
    main()
