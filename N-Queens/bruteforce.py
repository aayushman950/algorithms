import itertools

def is_valid(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if abs(i - j) == abs(perm[i] - perm[j]):
                return False
    return True

def n_queens_bruteforce(n):
    count = 0
    for perm in itertools.permutations(range(n)):
        if is_valid(perm):
            count += 1
    return count