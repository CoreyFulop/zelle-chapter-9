# blackjack_dealer.py

import random

def printIntro():
    print("This program simulates a blackjack dealer,")
    print("playing 'n' games as specified by the user.\n")

def getInput():
    n = eval(input("Enter the number of games to simulate: "))
    return n

def simulateNHands(n):
    busts = 0
    for i in range(n):
        outcome = simOneHand()
        if outcome == "bust":
            busts += 1
    return busts

def simOneHand():
    total = 0
    hasAce = False
    while not endHand(total):
        new_card = getCard()
        hasAce = checkForAce(new_card)
        total = updatePoints(total, new_card)
        total = checkAceHand(total, hasAce) # If ace is in hand, adds 10 to total if this results in stopping value
    if total > 21:
        outcome = "bust"
    else:
        outcome = "no bust"
    return outcome

def updatePoints(total, new_card):
    if new_card == "A":
        total += 1
    elif new_card == "J" or new_card == "Q" or new_card == "K":
        total += 10
    else:
        total += eval(new_card)
    return total

def checkAceHand(total, hasAce):
    if hasAce:
        if 17 <= total + 10 <= 21:
            return total + 10
        else:
            return total
    else:
        return total

def getCard():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return deck[random.randint(0,12)]

def checkForAce(new_card):
    return new_card == "A"

def endHand(total):
    return total >= 17

def printSummary(busts, n):
    print(f"In {n} games, there were {busts} dealer busts - {busts/n * 100:.2f}%.")

def main():
    printIntro()
    n = getInput()
    busts = simulateNHands(n)
    printSummary(busts, n)

if __name__ == "__main__":
    main()
    
