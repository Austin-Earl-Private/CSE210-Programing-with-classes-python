from week02.hilo.code.game.card import Card
from week02.hilo.code.game.card import GuessPosition


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.total_score = 0
        self.guess = GuessPosition.HIGHER


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        self.card.pullCard()
        print(f'The Card is: {self.card.getCardNumber()}')
        answer = input("Higher or Lower? [h/l] ")
        if answer == 'h':
            self.guess =  GuessPosition.HIGHER
        elif answer == 'l':
            self.guess = GuessPosition.LOWER

        # self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        self.card.pullCard()
        print(f'Next card was: {self.card.getCardNumber()}')

        if self.card.isGuessCorrect(self.guess):
            self.total_score += 100
        else:
            self.total_score -= 75



    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Your score is: {self.total_score}")
        if self.total_score < 0:
            self.is_playing = False
        else:
            response = input("Play again? [y/n] ")
            self.is_playing = response != 'n'
            print("")

