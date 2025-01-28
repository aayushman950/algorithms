import time
import matplotlib.pyplot as plt
from bruteforce import n_queens_bruteforce
from backtracking import n_queens_backtracking

def measure_time(func, n):
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start

def main():
    max_n = 12  # Brute-force becomes impractical beyond this
    ns = list(range(1, max_n))
    
    bf_times = []
    bt_times = []
    
    for n in ns:
        # Measure brute-force
        if n <= 10:  # Skip brute-force for n > 10
            bf_time = measure_time(n_queens_bruteforce, n)
            bf_times.append(bf_time)
        else:
            bf_times.append(None)
            
        # Measure backtracking
        bt_time = measure_time(n_queens_backtracking, n)
        bt_times.append(bt_time)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(ns[:len(bf_times)], bf_times, 'r-', label='Brute-Force', marker='o')
    plt.plot(ns, bt_times, 'b-', label='Backtracking', marker='s')
    plt.xlabel('Number of Queens (N)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('N-Queens Algorithm Comparison')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.savefig('queens_comparison.png')
    plt.show()

if __name__ == "__main__":
    main()