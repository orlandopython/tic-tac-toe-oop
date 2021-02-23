"""
Tic Tac Toe

This works and is a little more organized
There is not check for a valid input
It keeps going for 9 moves, even if there is a winner
"""

DEBUG = True  # a handy trick rather than 'assert' when learning


class TicTacToe:
    def __init__(self, filler: str = " "):
        self.players = ["X", "O"]
        self.board = [[filler] * 3, [filler] * 3, [filler] * 3]

    def get_next_player(self) -> str:
        return self.players[0]

    def move(self, player: str, row: int, col: int):
        self.board[row][col] = player
        self.players.reverse()  # sneaky and bad code

    def __repr__(self) -> str:
        return "\n".join("|".join(row) for row in self.board)


game = TicTacToe()

for i in range(9):  # there can be only 9 moves
    player = game.get_next_player()
    text = input(f"Player {player} enter the row and column as r,c : ")
    row, column = text.split(",")
    row = int(row)
    column = int(column)
    game.move(player, row, column)
    print(game)
