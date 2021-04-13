import random

class Character(Class):
    def __init__(self, name, race, gender, background, alignment, str, dex, con, intel, wis, char)
        self.name = name
        self.race = race
        self.gender = gender
        self.background = background
        self.alignment = alignment
        self.exp = 0
        self.str = 0
        self.dex = 0
        self.con = 0
        self.intel = 0
        self.wis = 0
        self.char = 0

    # Need a method to update attributes dynamically
    def updateAttr(self, stat, value):
        setattr(self, stat, value)

    # A roll method
    def roll(self, dieNumber, dieSize):
        for i in range(dieNumber):
            i = random.randint(1, dieSize)
            print(i)

    # Inventory/starting items
    


myCharacter = Character("Vesna", "Zaire", "neutral-evil", 0)
myCharacter.updateAttr("dexterity", 10)


# DnD Character Process Outline
# Choose a Race
# Determine Ability Scores
# Describe your character
    # Gender
    # Background
    # Alignment
    # Personal Characteristics
    # Height and Weight?
# Choose Equipment
    # Armor Class
    # Weapons
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#