def hamiltonian_backtracking(graph):
    n = len(graph)
    if n <= 1:
        return False
    path = [0]
    visited = [False] * n
    visited[0] = True

    def backtrack(current):
        if len(path) == n:
            return graph[current][0] == 1
        for v in range(n):
            if graph[current][v] and not visited[v]:
                visited[v] = True
                path.append(v)
                if backtrack(v):
                    return True
                # Backtrack
                path.pop()
                visited[v] = False
        return False

    return backtrack(0)