import itertools

def hamiltonian_bruteforce(graph):
    n = len(graph)
    if n <= 1:
        return False
    vertices = list(range(n))
    for perm in itertools.permutations(vertices[1:]):
        path = [0] + list(perm)
        valid = True
        # Check all consecutive edges
        for i in range(n-1):
            if not graph[path[i]][path[i+1]]:
                valid = False
                break
        # Check wrap-around edge
        if valid and graph[path[-1]][path[0]]:
            return True
    return False