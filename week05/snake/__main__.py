from week05.snake.game.casting.cast import Cast
from week05.snake.game.casting.food import Food
from week05.snake.game.casting.score import Score
from week05.snake.game.casting.snake import Snake
from week05.snake.game.directing.director import Director
from week05.snake.game.scripting.control_actors_action import ControlActorsAction
from week05.snake.game.scripting.draw_actors_action import DrawActorsAction
from week05.snake.game.scripting.handle_collisions_action import HandleCollisionsAction
from week05.snake.game.scripting.move_actors_action import MoveActorsAction
from week05.snake.game.scripting.script import Script
from week05.snake.game.services.keyboard_service import KeyboardService
from week05.snake.game.services.video_service import VideoService


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()