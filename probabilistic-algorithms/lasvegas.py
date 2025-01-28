import random

def lasvegas_nqueens(n, max_attempts=1000):
    def is_safe(board, row, col):
        for prev_col in range(col):
            if board[prev_col] == row or \
               abs(board[prev_col] - row) == abs(prev_col - col):
                return False
        return True

    for _ in range(max_attempts):
        board = [-1] * n
        for col in range(n):
            valid_rows = [row for row in range(n) if is_safe(board, row, col)]
            if not valid_rows:
                break  # Conflict found, restart
            board[col] = random.choice(valid_rows)
        if -1 not in board:
            return board  # Success
    return None  # Failure after max_attempts