import random

from week04.greed.game.casting.gem import Gem
from week04.greed.game.casting.rock import Rock
from week04.greed.game.shared.color import Color
from week04.greed.game.shared.point import Point


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        self._other_frame = True

        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._generate_random_collectable(cast)
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)



    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """


        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("player")
        collectables = cast.get_actors("collectables")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        move = self._other_frame
        for collectable in collectables:
            if player.get_position().equals(collectable.get_position()):
                self._score += collectable.get_points()
                cast.remove_actor("collectables", collectable)
                continue
            if move:
                collectable.move_next(max_x, max_y)


            if collectable.get_position().get_y() >= max_y - 2 * self._video_service.get_cell_size():
                cast.remove_actor("collectables", collectable)

        self._other_frame = not self._other_frame
        banner.set_text(f"Score: {self._score}")

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def _generate_random_collectable(self, cast):
        type = random.randint(0, 2)

        # message = messages[n]
        CELL_SIZE = self._video_service.get_cell_size()
        x = random.randint(1, self._video_service.get_width()/self._video_service.get_cell_size()-1)
        y = 1
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        if type == 1:
            collectable = Gem()
            text = "*"
        else:
            collectable = Rock()
            text = "o"
        collectable.set_text(text)
        collectable.set_font_size(15)
        collectable.set_color(color)
        collectable.set_position(position)
        # artifact.set_message(message)
        velocity = Point(0, 1)
        velocity = velocity.scale(CELL_SIZE)
        collectable.set_velocity(velocity)
        cast.add_actor("collectables", collectable)