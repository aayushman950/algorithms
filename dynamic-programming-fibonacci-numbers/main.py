# main.py

import time
import matplotlib.pyplot as plt
from traditional_fibonacci import Fibonacci as Fibonacci_iterative
from memoized_fibonacci import fibonacci_up_to_n as Fibonacci_memoized
from bottomup_fibonacci import fibonacci as Fibonacci_bottom_up

# Measure and plot the runtime for different Fibonacci approaches
def plot_runtime():
    n_values = list(range(1, 201))  # Test the function for n = 1 to 20
    times_iterative = []
    times_memoized = []
    times_bottom_up = []

    for n in n_values:
        # Iterative approach
        start_time = time.time()
        Fibonacci_iterative(n)
        end_time = time.time()
        times_iterative.append(end_time - start_time)

        # Memoized approach
        start_time = time.time()
        Fibonacci_memoized(n)
        end_time = time.time()
        times_memoized.append(end_time - start_time)

        # Bottom-up approach
        start_time = time.time()
        Fibonacci_bottom_up(n)
        end_time = time.time()
        times_bottom_up.append(end_time - start_time)

    # Plotting the results
    plt.plot(n_values, times_iterative, label='Iterative')
    plt.plot(n_values, times_memoized, label='Memoized')
    plt.plot(n_values, times_bottom_up, label='Bottom-Up')

    plt.title('Fibonacci Sequence Generation Time (Different Approaches)')
    plt.xlabel('Value of n')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.show()

# Driver Program
if __name__ == "__main__":
    plot_runtime()
