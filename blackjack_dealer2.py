# blackjack_dealer2.py

import random

def printIntro():
    print("This program simulates a blackjack dealer.\n")
    print("For each possible type of starting hand, 'n' hands are")
    print("played and the number of dealer busts are determined.\n")

def getInput():
    n = eval(input("Enter the number of hands to simulate per starting card type: "))
    return n

def simulateNHands(n, starting_card):
    busts = 0
    for i in range(n):
        outcome = simOneHand(starting_card)
        if outcome == "bust":
            busts += 1
    return busts

def simOneHand(starting_card):
    hasAce = False
    if starting_card == "A":
        total = 1
        hasAce = True
    elif starting_card == "F":
        total = 10
    else:
        total = eval(starting_card)
    while not endHand(total):
        new_card = getCard()
        hasAce = checkForAce(new_card, hasAce)
        total = updatePoints(total, new_card)
        total = checkAceHand(total, hasAce) # If ace in hand, add 10 points if results in stopping value
    if total > 21:
        outcome = "bust"
    else:
        outcome = "no bust"
    return outcome

def endHand(total):
    return total >= 17

def getCard():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return deck[random.randint(0,12)]

def checkForAce(new_card, hasAce):
    if hasAce == False:
        return new_card == "A"
    else:
        return hasAce    
    
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

def printSummary(card_types, data, n):
    print("Dealer starting card:\n")
    for i in range(len(data)):
        print(f"{card_types[i]:>2}: {data[i]:>3} busts from {n:3>} hands - {data[i]/n * 100:>6.2f}%.")

def main():
    printIntro()
    n = getInput()

    card_types = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "F"]
    data = []
    
    for starting_card in card_types:
        busts = simulateNHands(n, starting_card)
        data.append(busts)

    print()
    printSummary(card_types, data, n)

if __name__ == "__main__":
    main()

