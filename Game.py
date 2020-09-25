'''
Andrea "Nicci" Sheets
9/24/2020
Game 0 Assignment
'''

from MyUtilities import *

def InputTimes():
    while True:
        times = input("How many times would you like to roll your die? (Enter 0 if you would like to quit this application.) ")
        if times.isdigit():
            return times
            break   
        else:
            print("Please input a valid number.")
            continue     

def InputSides():
    while True:
        sides = input("How many sides would you like the die to have? ")
        if sides.isdigit() and int(sides) >= 2:
            return sides
            break
        else:
            print("Please input a valid number.")
            continue

def InputTarget():
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
            output = DieRoller(times, sides)
        elif target >= 1: 
            output = TargetRoller(times, sides, target)
        
        print(f"output is {output}")
                

Main()