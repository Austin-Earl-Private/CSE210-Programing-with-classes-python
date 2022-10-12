from week05.snake.game.scripting.action import Action


# TODO: Implement MoveActorsAction class here!
class MoveActorsAction(Action):
    def execute(self,cast,script):
        all_actors = cast.get_all_actors()
        for actor in all_actors:
            actor.move_next()

