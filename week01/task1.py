# Author: Austin Earl
from enum import Enum


class GameStyle(Enum):
    SIMPLE = 1,
    ADVANCED = 2


class Grid:
    empty_space = ' '

    def __init__(self, grid_x=3, grid_y=3, data=None):
        self.x = grid_x
        self.y = grid_y
        if data is None:
            data = []
            for i in range(0, self.x * self.y):
                data.append(self.empty_space)
        self.data = data

    def getSquare(self, number):
        self.__check_bounds(number)
        return self.data[number - 1]

    def setSquare(self, number, content):
        self.__check_bounds(number)
        if self.data[number - 1] == self.empty_space:
            self.data[number - 1] = content
        else:
            raise Exception(f"You can't place {content} here as there is already {self.data[number - 1]} here")
        return self.data[number - 1]

    def printGrid(self):
        square_counter = 1
        x_counter = 0
        y_counter = 0
        output_data = ""
        for ele in self.data:
            if x_counter == self.x:
                output_data += "\n"
                for x_pos in range(0, self.x):
                    if x_pos != 0:
                        output_data += "+"
                    output_data += "-"
                output_data += "\n"
                x_counter = 0
                y_counter += 1

            if x_counter != 0:
                output_data += "|"
            if ele == self.empty_space:
                ele = str(square_counter)
            output_data += ele
            x_counter += 1
            square_counter += 1

        print(output_data)

    def checkWin(self):
        square_counter = 1
        x_counter = 0
        y_counter = 0
        output_data = ""
        for ele in self.data:
            if x_counter == self.x:
                output_data += "\n"
                for x_pos in range(0, self.x):
                    if x_pos != 0:
                        output_data += "+"
                    output_data += "-"
                output_data += "\n"
                x_counter = 0
                y_counter += 1

            if x_counter != 0:
                output_data += "|"
            if ele == self.empty_space:
                ele = str(square_counter)
            output_data += ele
            x_counter += 1
            square_counter += 1

    def __check_bounds(self, number):
        if number < 1:
            raise Exception("Number out of range")
        if number > self.x * self.y:
            raise Exception("Number out of range")





def getGridSizeAdvanced():
    valid_x = False
    valid_y = False

    while not valid_x and not valid_y:
        if not valid_x:
            try:
                user_input_x = int(input("What is the Width of the play board?\n"))
                valid_x = True
            except ValueError:
                print("Only numbers are allowed.")
        if not valid_y:
            try:
                user_input_y = int(input("What is the Height of the play board?\n"))
                valid_y = True
            except ValueError:
                print("Only numbers are allowed.")

    return (user_input_x, user_input_y)


def setupMenu():
    valid = False;
    while not valid:
        user_input = input(
            f"""
    Welcome to Tic-Tac-Toe.
    Type "s" To start a simple 3 X 3 Grid Tic-Tac-Toe game
    Type "a" To create a custom Tic-Tac-Toe game\n""")
        if user_input.lower() != "s" or user_input.lower() != "a":
            if user_input.lower() == "s":
                return GameStyle.SIMPLE
            if user_input.lower() == "a":
                return GameStyle.ADVANCED
        else:
            print(f"{user_input} is not a valid input")
            continue

def main():
    game_style = setupMenu()
    if game_style == GameStyle.SIMPLE:
        grid = Grid(3,3)
    if game_style == GameStyle.ADVANCED:
        grid_size = getGridSizeAdvanced()
        grid = Grid(grid_size[0],grid_size[1])

    grid.printGrid()
    game_won = False


main()
