"""
Tic Tac Toe

This works but is extremely crude
No functions or classes
There is no check for a valid input
It keeps going for 9 moves, even if there is a winner sooner
"""

DEBUG = True  # a handy trick rather than 'assert' when learning
FILLER = " "
PLAYERS = ["X", "O"]

BOARD = [[FILLER] * 3, [FILLER] * 3, [FILLER] * 3]

for i in range(9):  # there can be only 9 moves
    player = PLAYERS[0]
    PLAYERS.reverse()  # this is not a good way even though it works
    text = input(f"Player {player} enter the row and column as r,c : ")
    row, column = text.split(",")
    row = int(row)
    column = int(column)
    if DEBUG:
        print(text, row, column)
    BOARD[row][column] = player
    for row in BOARD:
        print(row)
