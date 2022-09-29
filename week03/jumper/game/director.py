from week03.jumper.game.guesser import Guesser
from week03.jumper.game.parachute import Parachute
from week03.jumper.game.terminal_service import TerminalService
from week03.jumper.game.word_generator import WordGenerator


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._word_generator = WordGenerator()
        self._guesser = Guesser(self._word_generator.get_chosen_word())
        self._terminal_service = TerminalService()
        self._guess = ""
        self._guessed = False
        self._parachute = Parachute()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Get new guess and tries it

        Args:
            self (Director): An instance of Director.
        """
        letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._guess = letter

    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if not self._guesser.guess_letter(self._guess):
            self._parachute.remove_health(1)
        if self._guesser.checkForFullWord():
            self._guessed = True
            self._is_playing = False

    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        self._guesser.show_correct_letters()
        self._parachute.show_parachute()
        if self._parachute.get_health() <= 0:
            self._is_playing = False
        if not self._is_playing and self._guessed:
            self._terminal_service.write_text("Congrats! You Won!")