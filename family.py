from characters import characters
from random import randint

class Family:
    def __init__(self, members=None, speed_trait=False, character=None):
        if members:
            self.members = members
        else:
            self.members = set()
        self.speed_trait = speed_trait
        # self.character = "x"
        if character:
            self.character = character
        else:
            self.character = characters[randint(0, len(characters) - 1)]
