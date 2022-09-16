# Author: Austin Earl
# Content: Tic Tac Toe Game
# Description: A little Tic Tac Toe Game that might be a little over engineered. But it was fun to make. :P
from enum import Enum


class GameStyle(Enum):
    SIMPLE = 1,
    ADVANCED = 2


class Players(Enum):
    X = "X",
    O = "O"


class WinState(Enum):
    X = 1,
    O = 2,
    TIE = 3,
    NONE = 4


class Game:
    current_player = Players.X

    def __init__(self, grid):
        self.grid = grid
        self.max_size = grid.x * grid.y

    def startGame(self):
        win = WinState.NONE

        while win == WinState.NONE:
            try:
                self.grid.printGrid()

                square_number = self.__promptSquare()
                self.grid.setSquare(square_number, self.current_player.value[0])

                win = self.grid.checkWin()
                if win != WinState.NONE:
                    self.grid.printGrid()

                    if win == WinState.X or win == WinState.O:
                        print(f"{self.current_player.value[0]} Wins! Thanks For Playing!")
                    else:
                        print(f"It was a TIE! Thanks For Playing!")
                    break
                self.__changePlayer()
            except Exception as e:
                print(e)

    def __promptSquare(self):
        while True:
            try:
                return int(input(f"{self.current_player.value[0]}'s turn to choose a square (1-{self.max_size}): "))
            except ValueError:
                print("Only numbers are allowed.\n")

    def __changePlayer(self):
        if self.current_player == Players.X:
            self.current_player = Players.O
        else:
            self.current_player = Players.X


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
            self.data[number - 1] = content.upper()
        else:
            raise Exception(
                f"You can't place {content} on {number} as there is already {self.data[number - 1].value[0]} there")
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
                    for letter in str(y_counter * self.x + x_pos + 1):
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

        print(f"\n{output_data}\n")

    def checkWin(self):
        diagonal = self.__checkWinDiagonalCondition()
        column = self.__checkWinColumnCondition()
        row = self.__checkWinRowCondition()
        tie = self.__checkIfAllSquaresAreFilled()
        if diagonal[0]:
            return WinState[diagonal[1]]
        elif column[0]:
            return WinState[column[1]]
        elif row[0]:
            return WinState[row[1]]
        elif tie:
            return WinState.TIE
        else:
            return WinState.NONE

    def __checkWinRowCondition(self):
        temp = self.empty_space
        skip_row = False
        for index, ele in enumerate(self.data):
            if index % self.x == self.x - 1:
                if not skip_row and ele == temp:
                    return True, temp
                skip_row = False
                continue
            if ele == self.empty_space:
                skip_row = True
                continue
            # start of row
            if index % self.x == 0:
                temp = ele
            # element is not same as prev
            if temp != ele:
                skip_row = True

        return False, self.empty_space

    def __checkWinColumnCondition(self):
        temp = self.empty_space
        for x_pos in range(0, self.x):
            if self.data[x_pos] == self.empty_space:
                continue
            for y_pos in range(0, self.y):
                ele = self.data[y_pos * self.x + x_pos]
                if ele == self.empty_space:
                    break
                # start of row
                if y_pos == 0:
                    temp = ele
                # element is not same as prev
                if temp != ele:
                    break
                if y_pos == self.y - 1 and temp == ele:
                    return True, temp
        return False, self.empty_space

    def __checkIfAllSquaresAreFilled(self):
        for ele in self.data:
            if ele == self.empty_space:
                return False
        return True

    def __checkWinDiagonalCondition(self):
        # first diagonal top left
        temp = self.empty_space
        for x_pos in range(0, self.x):
            position = (x_pos * self.x) + x_pos
            ele = self.data[position]
            if ele == self.empty_space:
                break
            if x_pos == 0:
                temp = ele
            if temp != ele:
                break
            if x_pos == self.x - 1:
                return True, temp
        # second diagonal test bottom left
        temp = self.empty_space
        bottom_pos = (self.y - 1) * self.x
        for x_pos in range(0, self.x):
            position = bottom_pos - (x_pos * (self.x - 1))
            ele = self.data[position]
            if ele == self.empty_space:
                break
            if x_pos == 0:
                temp = ele
            if temp != ele:
                break
            if x_pos == self.x - 1:
                return True, temp
        return False, self.empty_space

    def __check_bounds(self, number):
        if number < 1:
            raise Exception("Number out of range")
        if number > self.x * self.y:
            raise Exception("Number out of range")


def getGridSizeAdvanced():
    while True:
        try:
            return int(input("What is the Size of the play board?\n"))

        except ValueError:
            print("Only numbers are allowed.")


def setupMenu():
    valid = False
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
        grid = Grid(3, 3)
    if game_style == GameStyle.ADVANCED:
        grid_size = getGridSizeAdvanced()
        grid = Grid(grid_size,grid_size)
    game = Game(grid)
    game.startGame()


main()
