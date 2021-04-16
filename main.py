#import character
from charOptions import race
from charOptions import raceList
from charOptions import charClassList
from charOptions import charClass
from charOptions import backgroundList
from charOptions import background
from charOptions import alignmentList
from charOptions import alignment
from character import Character
import random

def statRoll (dieNumber, dieSize):
        rolls = []
        for i in range(dieNumber):
            i = random.randint(1, dieSize)
            rolls.append(i)
        rolls.sort()
        return sum(rolls[3:0:-1])

def main():
    print("Welcome to the DnD Character Creator! This project is still in development  but any feedback is appreciated.")
    
    name = input("Let's start with your character's name: ")
    choiceGender = print(f'What gender will {name} be?: ')
    
    enumeratedRaceList = enumerate(raceList, 1)
    enumeratedCharClassList = enumerate(charClassList, 1)
    enumeratedBackgroundList = enumerate(backgroundList, 1)
    enumeratedAlignmentList = enumerate(alignmentList, 1)
    
    for count, r in enumeratedRaceList:
        print(count, r)
    choiceRace = input(f'What race will {name} be?: ')

    for count, c in enumeratedCharClassList:
        print(count, c)
    choiceClass = input(f'What class will {name} be?: ')

    for count, b in enumeratedBackgroundList:
        print(count, b)
    choiceBackground = input(f'What background will {name} have?: ')

    for count, a in enumeratedAlignmentList:
        print(count, a)
    choiceAlignment = input(f'What alignment will {name} be?: ')

    newCharacter = Character(name, choiceGender, choiceRace, choiceBackground, choiceAlignment, 20, 20, 20, 20, 20, 20)


    return newCharacter



    

newPlayer1 = main()
print(newPlayer1.str)
roll1 = statRoll(4, 6)
print(roll1)