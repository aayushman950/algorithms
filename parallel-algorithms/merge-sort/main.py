import time
import matplotlib.pyplot as plt
import numpy as np
from merge_sort import merge_sort
from parallel_merge_sort import parallel_merge_sort

def generate_random_array(size):
    return np.random.randint(0, size, size).tolist()

if __name__ == '__main__':
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7]
    sequential_times = []
    parallel_times = []
    
    for size in sizes:
        arr = generate_random_array(size)
        
        # Sequential Merge Sort
        start = time.time()
        merge_sort(arr.copy())
        sequential_time = time.time() - start
        sequential_times.append(sequential_time)
        
        # Parallel Merge Sort
        start = time.time()
        parallel_merge_sort(arr.copy())
        parallel_time = time.time() - start
        parallel_times.append(parallel_time)
        
        print(f"Size: {size}, Sequential: {sequential_time:.2f}s, Parallel: {parallel_time:.2f}s")
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, sequential_times, 'o-', label='Sequential Merge Sort')
    plt.plot(sizes, parallel_times, 's-', label='Parallel Merge Sort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Array Size (log scale)')
    plt.ylabel('Time (seconds, log scale)')
    plt.title('Comparison of Merge Sort Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig('merge_sort_comparison.png')
    plt.show()