'''
Andrea "Nicci" Sheets
9/27/2020
Game 0 Assignment - Take 2
'''

# This seems to run correctly, however it NEVER returns the individual dice that's rolled each time when I comment back in the print(roll) in the MyUtilities file, BUT the first Game.py code I wrote shows the individual dice rolled.  I can't see why this happens!!

from MyUtilities import *

def InputTimes():
    while True:
        times = input("How many times would you like to roll your die? (Enter 0 to quit the application.) ")
        try:
            times = int(times)
            return times
        except:
            print("Please use numeric digits.")
            continue
        if times < 0:
            print("Please enter a positive number.")
            continue
        break

def InputSides():        
    while True:
        sides = input("How many sides would you like the die to have? ")
        try: 
            sides = int(sides)
            return sides
        except:
            print("Please use numeric digits.")
            continue
        if sides <= 1:
            print("Please enter a positive number larger than 1.")
            continue
        break

def InputTarget():
    while True:
        target = input("What would you like the target number to be? ")
        try:
            target = int(target)
            return target
        except:
            print("Please use numeric digits.")
            continue
        break

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
