def n_queens_backtracking(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            count += backtrack(row+1, cols, diag1, diag2)
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)
        return count
    return backtrack(0, set(), set(), set())