import random

class Character():
    def __init__(self, name, gender, race, background, alignment, str, dex, con, intel, wis, char):
        self.name = name
        self.race = race
        self.gender = gender
        self.background = background
        self.alignment = alignment
        self.exp = 0
        self.str = str
        self.dex = dex
        self.con = con
        self.intel = intel
        self.wis = wis
        self.char = char

    # Need a method to update attributes dynamically
    def updateAttr(self, stat, value):
        setattr(self, stat, value)

    # A roll method

            

    # Inventory/starting items

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