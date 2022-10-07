import os
import random

from week04.greed.game.casting.actor import Actor
from week04.greed.game.casting.cast import Cast
from week04.greed.game.directing.director import Director
from week04.greed.game.services.keyboard_service import KeyboardService
from week04.greed.game.services.video_service import VideoService
from week04.greed.game.shared.color import Color
from week04.greed.game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(ROWS - 3)
    position = Point(x, y)
    position = position.scale(CELL_SIZE)
    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
    # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()

    # for n in range(DEFAULT_ARTIFACTS):

    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()