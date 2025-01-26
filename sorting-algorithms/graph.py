import time
import random
import matplotlib.pyplot as plt
from heap_sort import heap_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

import sys
sys.setrecursionlimit(1000000)


# Function to benchmark a given sorting algorithm
def benchmark_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

# Generate test cases
def generate_test_cases(size):
    best_case = list(range(size))  # Already sorted
    average_case = random.sample(range(size), size)  # Random shuffle
    worst_case = list(range(size, 0, -1))  # Reverse sorted
    return best_case, average_case, worst_case

# Plotting function
def plot_results(results, input_sizes, algorithms):
    cases = ["Best Case", "Average Case", "Worst Case"]
    
    for i, case in enumerate(cases):
        plt.figure(figsize=(10, 6))
        
        for algorithm in algorithms:
            plt.plot(input_sizes, [results[algorithm][size][i] for size in input_sizes], marker='o', label=algorithm)
        
        plt.title(f"{case} Runtime of Sorting Algorithms")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid()
        plt.show()

# Benchmark all algorithms
def main():
    algorithms = {
        "Heap Sort": heap_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Selection Sort": selection_sort,
    }

    input_sizes = [0, 10, 100, 500, 1000, 2000, 5000, 10000]  # Test for different sizes
    results = {name: {} for name in algorithms}

    for size in input_sizes:
        best_case, average_case, worst_case = generate_test_cases(size)

        for name, algorithm in algorithms.items():
            best_time = benchmark_sorting_algorithm(algorithm, best_case[:])  # Pass a copy
            avg_time = benchmark_sorting_algorithm(algorithm, average_case[:])  # Pass a copy
            worst_time = benchmark_sorting_algorithm(algorithm, worst_case[:])  # Pass a copy

            results[name][size] = (best_time, avg_time, worst_time)

    # Plot results
    plot_results(results, input_sizes, algorithms)

if __name__ == "__main__":
    main()
