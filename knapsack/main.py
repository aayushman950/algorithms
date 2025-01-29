import time
import random
import matplotlib.pyplot as plt
from bruteforce import knapsack_bruteforce
from bottomup import knapsack_bottom_up

def generate_items(n):
    values = [random.randint(1, 100) for _ in range(n)]
    weights = [random.randint(1, 10) for _ in range(n)]
    return values, weights

def main():
    max_n = 20
    test_cases = range(1, max_n + 1)
    brute_times = []
    dp_times = []

    for n in test_cases:
        capacity = 10 * n
        values, weights = generate_items(n)
        
        # Brute Force
        start = time.perf_counter()
        bf_max = knapsack_bruteforce(values, weights, capacity)
        brute_time = time.perf_counter() - start
        brute_times.append(brute_time)
        
        # Bottom-Up DP
        start = time.perf_counter()
        dp_max = knapsack_bottom_up(values, weights, capacity)
        dp_time = time.perf_counter() - start
        dp_times.append(dp_time)
        
        assert bf_max == dp_max, f"Discrepancy at n={n}"
        print(f"n={n}: BF {brute_time:.4f}s, DP {dp_time:.6f}s")

    plt.figure(figsize=(10, 6))
    plt.plot(test_cases, brute_times, 'o-', label='Brute Force')
    plt.plot(test_cases, dp_times, 's-', label='Bottom-Up DP')
    plt.xlabel('Number of Items')
    plt.ylabel('Execution Time (seconds)')
    plt.title('0/1 Knapsack Problem: Brute Force vs. Bottom-Up DP')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparison.png')
    plt.show()

if __name__ == "__main__":
    main()