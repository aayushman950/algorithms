# main.py

import time
import matplotlib.pyplot as plt
from traditional_fibonacci import Fibonacci

# Measure and plot the runtime for different values of n
def plot_runtime():
    n_values = list(range(1, 21))  # Test the function for n = 1 to 20
    times = []

    for n in n_values:
        start_time = time.time()
        Fibonacci(n)
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)

    plt.plot(n_values, times)
    plt.title('Fibonacci Sequence Generation Time')
    plt.xlabel('Value of n')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

# Driver Program
if __name__ == "__main__":
    plot_runtime()
