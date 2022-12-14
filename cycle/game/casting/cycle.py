from cycle import constants
from cycle.game.casting.actor import Actor
from cycle.game.shared.point import Point


class Cycle(Actor):
    """
    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self, starting_point, color,player_id):
        super().__init__()
        self._segments = []
        self._head_color = color
        self._tail_color = color
        self._player_id = player_id
        self._prepare_body(starting_point)

    def get_player_id(self):
        return self._player_id

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._tail_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def set_tail_color(self, color):
        self._tail_color = color

    def _prepare_body(self, startingPoint):
        velocity = Point(0, -1 * constants.CELL_SIZE)
        segment = Actor()
        segment.set_position(startingPoint)
        segment.set_velocity(velocity)
        segment.set_text("@")
        segment.set_color(self._head_color)
        self._segments.append(segment)
