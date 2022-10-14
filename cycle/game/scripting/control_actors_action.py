from cycle import constants
from cycle.game.scripting.action import Action
from cycle.game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        # self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        players = cast.get_actors("players")
        for player in players:
            direction = player.get_segments()[0].get_velocity()
            if player.get_player_id() == 1:
                if self._keyboard_service.is_key_down('a'):
                    direction = Point(-constants.CELL_SIZE, 0)

                # right
                if self._keyboard_service.is_key_down('d'):
                    direction = Point(constants.CELL_SIZE, 0)

                # up
                if self._keyboard_service.is_key_down('w'):
                    direction = Point(0, -constants.CELL_SIZE)

                # down
                if self._keyboard_service.is_key_down('s'):
                    direction = Point(0, constants.CELL_SIZE)
                player.turn_head(direction)
            if player.get_player_id() == 2:
                # left
                if self._keyboard_service.is_key_down('j'):
                    direction = Point(-constants.CELL_SIZE, 0)

                # right
                if self._keyboard_service.is_key_down('l'):
                    direction = Point(constants.CELL_SIZE, 0)

                # up
                if self._keyboard_service.is_key_down('i'):
                    direction = Point(0, -constants.CELL_SIZE)

                # down
                if self._keyboard_service.is_key_down('k'):
                    direction = Point(0, constants.CELL_SIZE)
                player.turn_head(direction)