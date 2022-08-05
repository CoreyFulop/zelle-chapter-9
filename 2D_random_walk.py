# 2D_random_walk.py

import random

def printIntro():
    print("This program simulates a 2D random walk.\n")

def getInput():
    n = eval(input("How many steps in the random walk: "))
    return n

def simNSteps(n):
    d1 = d2 = 0
    for i in range(n):
        step = random.randint(1, 4)
        if step == 1:
            d1 += 1
        elif step == 2:
            d1 -= 1
        elif step == 3:
            d2 += 1
        else: # step == 4
            d2 -= 1
    return d1, d2

def printSummary(d1, d2, n):
    print(f"\nAfter {n} steps, we have moved {d1} units in the first dimension,")
    print(f"and {d2} units in the second dimension for {d1 + d2} units total.\n")

    print(f"In a straight line, we have moved {(d1**2 + d2**2)**0.5:.2f} units.")

def main():
    printIntro()
    n = getInput()
    d1, d2 = simNSteps(n)
    printSummary(d1, d2, n)

if __name__ == "__main__":
    main()
