'''
Andrea "Nicci" Sheets
9/27/2020
Game 0 Assignment - Take 2
'''

from MyUtilities import *

def InputTimes():
    while True:
        times = input("How many times would you like to roll your die? (Enter 0 to quit the application.) ")
        try:
            times = int(times)
        except:
            print("Please use numeric digits.")
            continue
        if times < 0:
            print("Please enter a positive number.")
            continue
        elif times == 0:
            break
        break
    return times

def InputSides():        
    while True:
        sides = input("How many sides would you like the die to have? ")
        try: 
            sides = int(sides)
        except:
            print("Please use numeric digits.")
            continue
        if sides <= 1:
            print("Please enter a positive number larger than 1.")
            continue
        break
    return sides

def InputTarget():
    while True:
        target = input("What would you like the target number to be? ")
        try:
            target = int(target)
        except:
            print("Please use numeric digits.")
            continue
        if target < 0:
            print("Please enter a positive number.")
            continue
        break
    return target

def Main():
    while True:
        times = InputTimes()
        if times == 0:
            break
        sides = InputSides()
        target = InputTarget()
        if target == 0:
            output = "The sum of all dice rolled is "+str(DieRoller(times, sides))+"."
        elif target > 0: 
            output = "The total number of times the dice rolled greater than or equal to the target number is "+str(TargetRoller(times, sides, target))+"."
        print("\n"+ output +"\n")

Main()
