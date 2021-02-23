"""
Tic Tac Toe

This used the model, view, controller (MVC) design pattern
There is no check for a valid input
It keeps going for 9 moves, even if there is a winner
"""

from typing import List, Tuple


DEBUG = True  # a handy trick rather than 'assert' when learning


class Player:
    def __init__(self, name: str):
        self.name = name
        self.prompt = f"\t\tPlayer {name} enter the row and column as r,c : "
        # faster than creating the prompt each move

    def get_move(self) -> Tuple[int, int]:
        text = input(self.prompt)
        row, column = [int(x) for x in text.split(",")]
        return row, column

    def __repr__(self) -> str:
        return self.name


class GameModel:  # Contains the data and a way to update it
    def __init__(self, size: int = 3, filler: str = " "):
        self.size = size
        self.data = [[filler for _ in range(size)] for _ in range(size)]

    def move(self, player: Player, row: int, column: int):
        self.data[row][column] = player

    def get_row(self, row: int) -> List[int]:
        return self.data[row]


class GameView:  # overkill but illustrates the MVC idea; useful for more complex game like monopoly
    def __init__(self, model: GameModel):
        self.model = model

    def __repr__(self) -> str:
        lines_of_text = []  # faster to append to a list that append to text
        for i in range(self.model.size):
            row = self.model.get_row(i)
            aline_of_text = "|".join(str(cell) for cell in row)
            lines_of_text.append(aline_of_text)
        return "\n".join(lines_of_text)  # a block of next


class TicTacToeGameController:
    def __init__(self, size: int = 3, filler: str = " ", players: List[Player] = None):
        self.players = players or []
        self.index = 0
        self.model = GameModel(size=size, filler=filler)
        self.view = GameView(self.model)
        self.move_counter = size * size

    def make_next_move(self) -> bool:
        player = self.players[self.index]
        self.index = (self.index + 1) % 2
        row, col = player.get_move()
        self.model.move(player, row, col)
        self.move_counter -= 1
        return self.move_counter > 0  # overkill but good for clarity

    def __repr__(self) -> str:
        return str(self.view)


players = [Player(name="X"), Player(name="O")]
game = TicTacToeGameController(size=3, filler=" ", players=players)

while game.make_next_move():
    print(game)
