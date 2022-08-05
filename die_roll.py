# die_roll.py

import random

def printIntro():
    print("This program simulates rolling five six-sided die,")
    print("and prints the number of times five-of-a-kind are rolled.\n")

def getIntro():
    n = eval(input("Enter the number of times to roll the five die: "))
    return n

def simNRolls(n):
    five_of_a_kind = 0
    for i in range(n):
        d1 = rollDie()
        d2 = rollDie()
        d3 = rollDie()
        d4 = rollDie()
        d5 = rollDie()
        if d1 == d2 == d3 == d4 == d5:
            five_of_a_kind += 1
    return five_of_a_kind

def rollDie():
    outcome = random.randint(1, 6)
    return outcome

def printSummary(five_of_a_kind, n):
    print(f"\nIn {n} rolls of five die, there were {five_of_a_kind} instances")
    print(f"where all five die gave the same number - {five_of_a_kind/n * 100:.2f}%")

def main():
    printIntro()
    n = getIntro()
    five_of_a_kind = simNRolls(n)
    printSummary(five_of_a_kind, n)

if __name__ == "__main__":
    main()
