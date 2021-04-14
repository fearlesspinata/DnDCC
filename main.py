#import character

race = ['Dwarf', 'Elf', 'Halfling', 'Human']
charClass = ['Bard', 'Cleric', 'Fighter', 'Rogue', 'Wizard']
background = ['Acolyte', 'Criminal', 'Entertainer', 'Soldier']

print("Welcome to the DnD Character Creator! This project is still in development  but any feedback is appreciated.")
name = input("Let's start with your character's name: ")
print(f'What race will {name} be?')
enumeratedRace = enumerate(race, 1)
for count, r in enumeratedRace:
    print(count, r)

choiceRace = input()

if choiceRace == '1':
    choiceRace = "Dwarf"
if choiceRace == '2':
    choiceRace = "Elf"
if choiceRace == '3':
    choiceRace = "Halfling"
if choiceRace == '4':
    choiceRace = "Human"

print(f'So {name} will be a {choiceRace}?')