board = [
    [0, 0, 0, 0, 0],
    [0, '*', 0, 0, 0],
    [0, 0, '*', 0, 0],
    [0, 0, '*', 0, 0],
    [0, 0, 0, 0, 0],
]

x = 1
y = 1
for row in board[1:len(board) - 1]:
    for column in row[1:len(row) - 1]:
        if board[x][y] == '*':
            if board[x + -1][y + 1] != '*':
                board[x + -1][y + 1] += 1
            if board[x + 0][y + 1] != '*':
                board[x + 0][y + 1] += 1
            if board[x + 1][y + 1] != '*':
                board[x + 1][y + 1] += 1
            if board[x + -1][y + 0] != '*':
                board[x + -1][y + 0] += 1
            if board[x + 1][y + 0] != '*':
                board[x + 1][y + 0] += 1
            if board[x + -1][y + -1] != '*':
                board[x + -1][y + -1] += 1
            if board[x + 0][y + -1] != '*':
                board[x + 0][y + -1] += 1
            if board[x + 1][y + -1] != '*':
                board[x + 1][y + -1] += 1
        y += 1
    y = 1
    x += 1
x = 1

for row in board[1:4]:
    print(row[1:4])