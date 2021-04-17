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
        return sum(rolls[len(rolls) - 1:0:-1])
def checkAbility(choiceAbility, value):
    if choiceAbility.lower() == "strength":
        strength = value
        return strength
    elif choiceAbility.lower() == "dexterity":
        dexterity = value
        return dexterity
    elif choiceAbility.lower() == "constitution":
        constitution = value
        return constitution
    elif choiceAbility.lower() == "intelligence":
        intelligence = value
        return intelligence
    elif choiceAbility.lower() == "wisdom":
        wisdom = value
        return wisodm
    elif choiceAbility.lower() == "charisma":
        charisma = value
        return charisma
    

def main():
    print("Welcome to the DnD Character Creator! This project is still in development  but any feedback is appreciated.")
    
    name = input("Let's start with your character's name: ")
    choiceGender = print(f'What gender will {name} be?: ')
    
    enumeratedRaceList = enumerate(raceList, 1)
    enumeratedBackgroundList = enumerate(backgroundList, 1)
    enumeratedAlignmentList = enumerate(alignmentList, 1)
    
    for count, r in enumeratedRaceList:
        print(count, r)
    choiceRace = input(f'What race will {name} be?: ')

    for count, b in enumeratedBackgroundList:
        print(count, b)
    choiceBackground = input(f'What background will {name} have?: ')

    for count, a in enumeratedAlignmentList:
        print(count, a)
    choiceAlignment = input(f'What alignment will {name} be?: ')

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
            roll + str(i) = statRoll(4, 6)
            print(roll + str(i))
            choiceAbility = input("What ability will you assign these points to?: ")
            choice + str(i) = checkAbility(choiceAbility, roll+str(i))

            
    else:
        choiceRoll = 'Choose'


    



    # newCharacter = Character(name, choiceGender, choiceRace, choiceBackground, choiceAlignment, 20, 20, 20, 20, 20, 20)
    # return newCharacter



    

newPlayer1 = main()
roll1 = statRoll(4, 6)
print(roll1)
