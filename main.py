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
import yaml
import random
import json
import pprint

def addModifiers(character):
    charRace = character.race
    with open("C:\\Users\\vesna\\Programming\\DnDcc\\raceMods.yaml") as f:
        abilityDict = yaml.load(f, Loader=yaml.FullLoader)
        abilityDict = abilityDict['races']['name'][charRace]['Bonus']
        character.str += abilityDict['str']
        character.dex += abilityDict['dex']
        character.con += abilityDict['con']
        character.wis += abilityDict['wis']
        character.intel += abilityDict['intel']
        character.char += abilityDict['cha']
    
    return character

def statRoll (dieNumber, dieSize):
        rolls = []
        for i in range(dieNumber):
            i = random.randint(1, dieSize)
            rolls.append(i)
        rolls.sort()
        return sum(rolls[len(rolls) - 1:0:-1])
    

def main():
    print("Welcome to the DnD Character Creator! This project is still in development  but any feedback is appreciated.")
    
    name = input("Let's start with your character's name: ")
    choiceGender = input(f'What gender will {name} be?: ')
    
    enumeratedRaceList = enumerate(raceList, 1)
    enumeratedBackgroundList = enumerate(backgroundList, 1)
    enumeratedAlignmentList = enumerate(alignmentList, 1)
    statChoices = {'str': 0, 'dex': 0, 'int': 0, 'wis': 0, 'cha': 0}
    
    for count, r in enumeratedRaceList:
        print(count, r)
    choiceRace = input(f'What race will {name} be?: ')
    choiceRace = raceList[int(choiceRace) -1]

    for count, b in enumeratedBackgroundList:
        print(count, b)
    choiceBackground = input(f'What background will {name} have?: ')
    choiceBackground = backgroundList[int(choiceBackground) -1]

    for count, a in enumeratedAlignmentList:
        print(count, a)
    choiceAlignment = input(f'What alignment will {name} be?: ')
    choiceAlignment = alignmentList[int(choiceAlignment) -1]

    print("Now that we've gotten the basics taken care of let's move on to abilites")
    choiceRoll = input("""For starters what would you prefer to use to determine your stats? \n
    1. Roll
    2. Choose for myself
    """)

    if choiceRoll == '1':
        choiceRoll = 'roll'
        print("""You've chosen to roll for you ability points. For those new to Dungeons and Dragons \n
        this process will include rolling a 4d6, and taking the sum of the top 3 highest numbers and assigning it \n
        to an ability (strength, dexterity, constitution, intelligence, wisdom, and charisma). The rolling \n
        of the 4d6 aas well as taking the sum will be done for you and you will choose which ability stat \n
        to assign the value to. Let's get started.""")
        
        for i in range(6):
            i = statRoll(4, 6)
            print(f'You rolled a {i}')
            statChoice = input('What ability will you want to assign this value to?')
            statChoices[statChoice] = i
            print(statChoices[statChoice])
    else:
        choiceRoll = 'Choose'

    newCharacter = Character(name, choiceGender, choiceRace, choiceBackground, choiceAlignment, statChoices['str'], statChoices['dex'], statChoices['con'], statChoices['intel'], statChoices['wis'], statChoices['cha'])
    return newCharacter

newPlayer1 = main()
addModifiers(newPlayer1)
print(newPlayer1.con)