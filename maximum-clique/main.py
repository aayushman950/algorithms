import time
import random
import matplotlib.pyplot as plt
from bruteforce import max_clique_bruteforce
from branchandbound import max_clique_branch_and_bound

def generate_graph(n, edge_prob=0.5):
    """Generate random undirected graph with n nodes"""
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < edge_prob:
                graph[i][j] = 1
                graph[j][i] = 1
    return graph

def main():
    max_n = 15  # Brute force becomes impractical beyond this
    test_cases = range(1, max_n + 1)
    brute_times = []
    bb_times = []

    for n in test_cases:
        graph = generate_graph(n, edge_prob=0.6)
        
        # Brute Force
        start = time.perf_counter()
        bf_size = max_clique_bruteforce(graph)
        brute_time = time.perf_counter() - start
        brute_times.append(brute_time)
        
        # Branch and Bound
        start = time.perf_counter()
        bb_size = max_clique_branch_and_bound(graph)
        bb_time = time.perf_counter() - start
        bb_times.append(bb_time)
        
        assert bf_size == bb_size, f"Discrepancy at n={n}: BF={bf_size} vs BB={bb_size}"
        print(f"n={n}: BF {brute_time:.4f}s, BB {bb_time:.6f}s")

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(test_cases, brute_times, 'o-', label='Brute Force')
    plt.plot(test_cases, bb_times, 's-', label='Branch & Bound')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Maximum Clique Problem: Brute Force vs Branch & Bound')
    plt.legend()
    plt.grid(True)
    plt.savefig('clique_comparison.png')
    plt.show()

if __name__ == "__main__":
    main()