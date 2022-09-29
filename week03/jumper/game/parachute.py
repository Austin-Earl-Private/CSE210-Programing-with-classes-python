class Parachute:

    def __init__(self):
        self._health = 4
        self._parachute = ["   _____", "  /_____\\", "  \     /", "   \   /"]

    def get_health(self):
        return self._health

    def remove_health(self, points):
        self._health -= points

    def show_parachute(self):
        for line in range(4 - self._health, 4):
            print(self._parachute[line])
        if self._health <= 0:
            print("     X")
        else:
            print("     0")
        print("""    /|\\
     |
    / \\
    
^^^^^^^^^^^    """)

#   _____
#  /_____\
#  \     /
#   \   /
#     0
#    /|\
#     |
#    / \
#
