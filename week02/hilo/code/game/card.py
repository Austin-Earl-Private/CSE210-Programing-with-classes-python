import random
from enum import Enum


class GuessPosition(Enum):

    HIGHER = 1,
    LOWER = 2,


class Card:
    """Basic card class

        Card hold previous card and current card numbers

        Attributes:
            card_number (int): The current card_number
            old_card_number (int): The previous card number
        """
    def __init__(self):
        """Constructs a new Card.

                Args:
                    self (Card): an instance of Card.
        """
        self.card_number = random.randint(1, 14)
        self.old_card_number = random.randint(1, 14)

    def getCardNumber(self):
        """gets the current card number

                Args:
                    self (Card): an instance of Card.
        """
        return self.card_number

    def pullCard(self):
        """Pulls a new card and randomizes the number
        Copies card number to old card number

                        Args:
                            self (Card): an instance of Card.
        """
        self.old_card_number = self.card_number
        self.card_number = random.randint(1, 14)

    def isGuessCorrect(self, position):
        """Check old card number verses current card number against users guess

                                Args:
                                    self (Card): an instance of Card.
                """
        if position == GuessPosition.HIGHER:
            return self.card_number > self.old_card_number
        elif position == GuessPosition.LOWER:
            return self.card_number < self.old_card_number
