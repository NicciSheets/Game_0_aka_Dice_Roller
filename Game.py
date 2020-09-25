'''
Andrea "Nicci" Sheets
9/24/2020
Game 0 Assignment
'''

from MyUtilities import *

def InputTimes():
    #Input validation for user input for amount of times dice rolled - ensures it is a digit
    while True:
        times = input("How many times would you like to roll your die? (Enter 0 to quit the application.) ")
        if times.isdigit():
            return times
            break   
        else:
            print("Please input a valid number.")
            continue     

def InputSides():
    #Input validation for user input for how many sides the die has - ensures it is a digit and is also a number larger than 1 (doesn't allow 1 or 0).
    while True:
        sides = input("How many sides would you like the die to have? (Enter a number larger than 1.) ")
        if sides.isdigit() and int(sides) >= 2:
            return sides
            break
        else:
            print("Please input a valid number.")
            continue

def InputTarget():
    #Input validation for user input for the desired target number - ensures it is a digit
    while True:
        target = input("What would you like the target number to be? ")
        if target.isdigit():
            return target
            break
        else:
            print("Please input a valid number.")
            continue

def Main():
    while True:
        times = int(InputTimes())
        if times == 0:
            break
        sides = int(InputSides())
        target = int(InputTarget())
        if target == 0:
            output = "The sum of all dice rolled is "+str(DieRoller(times, sides))+"."
        elif target > 0: 
            output = "The total number of times the dice rolled greater than or equal to the target number is "+str(TargetRoller(times, sides, target))+"."
        print("\n"+ output +"\n")


Main()