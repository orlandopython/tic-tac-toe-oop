FILLER = "   "
print("================== a common newbie mistake ==================")
ROW = [FILLER] * 3

BOARD = [
    ROW,  # THIS WILL NOT WORK, WHY?
    ROW,
    ROW,
]


BOARD[1][1] = "$$$"
for row in BOARD:
    print(row)  # we created a board containing 3 references to the same row


input("Press any key to continue")
print("================== do it right ==================")

BOARD = [[FILLER] * 3, [FILLER] * 3, [FILLER] * 3]

# This does the same thing
# SIZE = 3
# BOARD = [[FILLER for i in range(SIZE)] for i in range(SIZE)]


BOARD[0][0] = "==="
BOARD[1][1] = "$$$"
BOARD[2][2] = "???:"
for row in BOARD:
    print(row)  # now each row is different
