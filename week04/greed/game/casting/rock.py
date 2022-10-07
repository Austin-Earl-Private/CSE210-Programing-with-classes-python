from week04.greed.game.casting.actor import Actor
from week04.greed.game.casting.collectable import Collectable


class Rock(Collectable):

    def __init__(self):
        super().__init__(-1)

