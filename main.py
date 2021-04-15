#import character
from charOptions import race
from charOptions import raceList
from charOptions import charClassList
from charOptions import charClass
from charOptions import backgroundList
from charOptions import background

def main():
    print("Welcome to the DnD Character Creator! This project is still in development  but any feedback is appreciated.")
    
    name = input("Let's start with your character's name: ")
    
    enumeratedRaceList = enumerate(raceList, 1)
    enumeratedCharClassList = enumerate(charClassList, 1)
    enumeratedBackgroundList = enumerate(backgroundList, 1)
    for count, r in enumeratedRaceList:
        print(count, r)

    for count, c in enumeratedCharClassList:
        print(count, c)

    for count, b in enumeratedBackgroundList:
        print(count, b)



    

    print(f'So far {name} is a {choiceRace}. Is this correct?: ')




main()