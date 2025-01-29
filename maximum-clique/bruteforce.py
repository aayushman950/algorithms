import itertools

def max_clique_bruteforce(graph):
    n = len(graph)
    if n == 0:
        return 0
    vertices = list(range(n))
    
    # Check cliques from largest to smallest
    for k in range(n, 0, -1):
        for subset in itertools.combinations(vertices, k):
            if is_clique(subset, graph):
                return k
    return 1  # Edge case: empty graph

def is_clique(subset, graph):
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            if not graph[subset[i]][subset[j]]:
                return False
    return True