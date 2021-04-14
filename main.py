#import character
from charOptions import race
from charOptions import raceList
from charOptions import charClass
from charOptions import background

def main():
    print("Welcome to the DnD Character Creator! This project is still in development  but any feedback is appreciated.")
    
    name = input("Let's start with your character's name: ")
    enumeratedList = enumerate(raceList, 1)
    for count, r in enumeratedList:
        print(count, r)

    choiceRace = input(f'What race will {name} be?: ')
    choiceRace = race[choiceRace]

    print(f'So far {name} is a {choiceRace}. Is this correct?: ')




main()