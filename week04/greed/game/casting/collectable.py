from week04.greed.game.casting.actor import Actor


class Collectable(Actor):

    def __init__(self, points):
        super().__init__()
        self._points = points

    def set_points(self,points):
        self._points = points

    def get_points(self):
        return self._points