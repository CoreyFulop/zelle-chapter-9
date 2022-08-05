# random_walk.py

import random

def printIntro():
    print("This program simualtes simple random walks, in a single dimension.\n")

def getNumberOfWalks():
    m = eval(input("How many walks to simulate: "))
    return m

def getStepsInput():
    n = eval(input("How many steps to take per random walk: "))
    return n

def simMRandomWalks(m, n):
    total_dist = 0
    for i in range(m):
        dist = randomNWalk(n)
        total_dist += dist
    return total_dist

def randomNWalk(n):
    dist = 0
    for i in range(n):
        coin = random.randint(0, 1)
        if coin == 1: # "Heads"
            dist += 1
        else: # coin == 0 "Tails"
            dist -= 1
    return dist

def printSummary(total_dist, m, n):
    print(f"\nIn {m} random walks of {n} steps, the average distance moved is {total_dist/m:.2f} steps.")

def main():
    printIntro()
    m = getNumberOfWalks()
    n = getStepsInput()
    total_dist = simMRandomWalks(m, n)
    printSummary(total_dist, m , n)

if __name__ == "__main__":
    main()
