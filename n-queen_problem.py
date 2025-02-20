
# Backtracking: N-Queens Problem

def solve_n_queens(n):
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def place_queen(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                place_queen(row + 1)
                board[row] = -1

    place_queen(0)
    return solutions
