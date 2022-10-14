from cycle import constants
from cycle.game.casting.cast import Cast
from cycle.game.casting.cycle import Cycle
from cycle.game.casting.score import Score
from cycle.game.directing.director import Director
from cycle.game.scripting.control_actors_action import ControlActorsAction
from cycle.game.scripting.draw_actors_action import DrawActorsAction
from cycle.game.scripting.handle_collisions_action import HandleCollisionsAction
from cycle.game.scripting.move_actors_action import MoveActorsAction
from cycle.game.scripting.script import Script
from cycle.game.services.keyboard_service import KeyboardService
from cycle.game.services.video_service import VideoService
from cycle.game.shared.point import Point


def main():
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food())
    third_width = int(constants.MAX_X / 3)
    half_height = int(constants.MAX_Y / 2)
    cast.add_actor("players", Cycle(Point(third_width, half_height), constants.RED, 1))
    cast.add_actor("players", Cycle(Point(third_width * 2, half_height), constants.GREEN, 2))

    p2_score = Score()
    p2_score.set_position(Point(third_width * 2, 0))
    cast.add_actor("scores", Score())
    cast.add_actor("scores", p2_score)

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
