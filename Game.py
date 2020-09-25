'''
Andrea "Nicci" Sheets
9/24/2020
Game 0 Assignment
'''

from MyUtilities import *

# print(DieRoller(5, 6))
# print(TargetRoller(5,6,1))

def InputTimes():
    while True:
        times = input("How many times would you like to roll your die? (Enter 0 if you would like to quit this application.) ")
        # print(times)
        if times.isdigit():
            return times
            break   
        else:
            print("Please input a valid number.")
            continue        



# sides = input("How many sides would you like the die to have? **Cannot be less than 1! ")
# print(sides)

def InputSides():
    while True:
        sides = input("How many sides would you like the die to have? ")
        if sides.isdigit() and int(sides) >= 2:
            return sides
            break
        else:
            print("Please input a valid number.")
            continue


# target = input("What would you like the target number to be? ")
# print(target)

def InputTarget():
    while True:
        target = input("What would you like the target number to be? ")
        if target.isdigit():
            return target
            break
        else:
            print("Please input a valid number.")
            continue


# print(InputTimes())
# print(InputSides())
# print(InputTarget())

print(TargetRoller(int(InputTimes()), int(InputSides()), int(InputTarget())))

