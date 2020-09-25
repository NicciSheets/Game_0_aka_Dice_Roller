'''
Andrea Sheets
2020_9_21
MyUtilies
Die Roller
'''

import random
import os

def DieRoller(times, sides):
    # rolls any amount of dice (times) with any amount of sides (sides) and returns the sum of all die rolled, using an accumulator (total)
    total = 0
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
        # print(roll) #Had this for testing purposes - can comment back in to see the numbers rolled for each iteration
    return total

def TargetRoller(times, sides, target):
    # rolls any amount of dice (times) with any amount of sides (sides) and returns how many times a roll was either equal to or greater than a target number (target)
    total = 0
    for i in range(times):
        roll = random.randint(1, sides)
        # print(roll) #Had this for testing purposes = can comment back in to see the numbers rolled for each iteration
        if roll >= target:
            total += 1
    return total


    