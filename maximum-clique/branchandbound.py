def max_clique_branch_and_bound(graph):
    n = len(graph)
    if n == 0:
        return 0
    best_size = [0]  # Using list to allow modification in nested function
    
    def backtrack(current_clique, candidates):
        # Update best size if current clique is larger
        if len(current_clique) > best_size[0]:
            best_size[0] = len(current_clique)
        
        # Prune if remaining candidates can't improve the solution
        if len(current_clique) + len(candidates) <= best_size[0]:
            return
        
        for i, node in enumerate(candidates):
            # Check if node is connected to all nodes in current clique
            if all(graph[node][v] for v in current_clique):
                # Generate new candidates: nodes after current one connected to 'node'
                new_candidates = [v for v in candidates[i+1:] if graph[v][node]]
                backtrack(current_clique + [node], new_candidates)
    
    backtrack([], list(range(n)))
    return best_size[0] if best_size[0] > 0 else 1