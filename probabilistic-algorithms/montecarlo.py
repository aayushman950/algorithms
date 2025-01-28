import random

def montecarlo_nqueens(n, max_trials=1000):
    def is_valid(board):
        for col in range(n):
            for prev_col in range(col):
                if board[prev_col] == board[col] or \
                   abs(board[prev_col] - board[col]) == abs(prev_col - col):
                    return False
        return True

    for _ in range(max_trials):
        board = [random.randint(0, n-1) for _ in range(n)]
        if is_valid(board):
            return board  # Success
    return None  # Failure after max_trials