import time
import matplotlib.pyplot as plt
from bruteforce import hamiltonian_bruteforce
from backtracking import hamiltonian_backtracking

def generate_graph(n):
    # Generates a path graph without Hamiltonian cycle
    graph = [[0]*n for _ in range(n)]
    if n <= 1:
        return graph
    for i in range(n-1):
        graph[i][i+1] = 1
        graph[i+1][i] = 1
    # Ensure no cycle for n >= 2
    if n == 2:
        graph[0][1] = graph[1][0] = 0
    return graph

def main():
    max_n = 11  # Warning: Brute force becomes very slow for n > 10
    test_cases = range(2, max_n+1)
    brute_times = []
    backtrack_times = []

    for n in test_cases:
        graph = generate_graph(n)
        
        # Brute Force
        start = time.perf_counter()
        bf_result = hamiltonian_bruteforce(graph)
        brute_time = time.perf_counter() - start
        brute_times.append(brute_time)
        
        # Backtracking
        start = time.perf_counter()
        bt_result = hamiltonian_backtracking(graph)
        backtrack_time = time.perf_counter() - start
        backtrack_times.append(backtrack_time)
        
        assert bf_result == bt_result, f"Discrepancy at n={n}"
        print(f"n={n}: BF {brute_time:.4f}s, BT {backtrack_time:.6f}s")

    plt.figure(figsize=(10, 6))
    plt.plot(test_cases, brute_times, 'o-', label='Brute Force')
    plt.plot(test_cases, backtrack_times, 's-', label='Backtracking')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Hamiltonian Cycle: Brute Force vs. Backtracking')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparison.png')
    plt.show()

if __name__ == "__main__":
    main()