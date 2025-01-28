# main.py
import time
import matplotlib.pyplot as plt
from recursion import fib as fib_recursive
from memoization import fib as fib_memoization, reset_cache
from bottomup import fib as fib_bottomup

def measure_time(func, n, reset=False):
    if reset:
        reset_cache()  # Reset cache before timing memoization
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start

def main():
    # Test ranges
    small_n = list(range(5, 35, 5))    # For recursion (n ≤ 30)
    large_n = list(range(100, 3001, 200))  # For memoization/bottom-up (n ≤ 2000)

    # Measure recursive (no reset needed)
    recursive_times = [measure_time(fib_recursive, n) for n in small_n]

    # Measure memoization (reset before each run)
    memo_times = [measure_time(fib_memoization, n, reset=True) for n in large_n]

    # Measure bottom-up (no reset needed)
    bottomup_times = [measure_time(fib_bottomup, n) for n in large_n]

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(small_n, recursive_times, 'ro-', label='Recursive (O(2^N))')
    plt.plot(large_n, memo_times, 'g*-', label='Memoization (O(N))')
    plt.plot(large_n, bottomup_times, 'b^-', label='Bottom-up (O(N))')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Fibonacci Algorithm Time Complexity Comparison')
    # plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.savefig('comparison_linearscale.png')
    plt.show()

if __name__ == "__main__":
    main()