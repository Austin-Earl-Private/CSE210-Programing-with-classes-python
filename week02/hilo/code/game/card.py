import random
from enum import Enum


class GuessPosition(Enum):
    HIGHER = 1,
    LOWER = 2,


class Card:

    def __init__(self):
        self.card_number = random.randint(1, 14)
        self.old_card_number = random.randint(1, 14)

    def getCardNumber(self):
        return self.card_number

    def pullCard(self):
        self.old_card_number = self.card_number
        self.card_number = random.randint(1, 14)

    def isGuessCorrect(self, position):
        if position == GuessPosition.HIGHER:
            return self.card_number > self.old_card_number
        elif position == GuessPosition.LOWER:
            return self.card_number < self.old_card_number
