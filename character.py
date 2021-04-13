import random

class Character:
    def __init__(self, playerName, characterName, alignment, exp):
        self.playerName = playerName
        self.characterName = characterName
        self.alignment = alignment
        self.exp = exp
        self.hitPoints = 10
        self.armorClass = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisodm = 0
        self.charisma = 0

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