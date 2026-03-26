#Task 7
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == "Q":
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < 4 and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1
    return True

def solve(board, col):
    if col >= 4:
        return True
    for row in range(4):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            if solve(board, col + 1):
                return True
            board[row][col] = "_"
    return False

board = [["_" for _ in range(4)] for _ in range(4)]
if solve(board, 0):
    for row in board:
        print(" ".join(row))
else:
    print("No solution")
