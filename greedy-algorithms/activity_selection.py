import time
import matplotlib.pyplot as plt
import random

# Activity Selection Algorithm
def printMaxActivities(s, f):
    n = len(f)
    i = 0  # Index of the first activity

    # Selected activities
    selected_activities = [i]

    # Consider the rest of the activities
    for j in range(1, n):
        if s[j] >= f[i]:
            selected_activities.append(j)
            i = j

    return selected_activities

# Generate random test cases
def generate_test_case(n):
    activities = []
    
    # Generate random start and finish times
    for _ in range(n):
        start = random.randint(0, 100)
        finish = start + random.randint(1, 10)
        activities.append((start, finish))
    
    # Sort activities by finish time
    activities.sort(key=lambda x: x[1])  # Sort by finish time
    
    # Separate start and finish times
    s = [a[0] for a in activities]
    f = [a[1] for a in activities]
    return s, f

# Measure running time
def measure_running_time():
    input_sizes = list(range(10, 1001, 50))  # Input sizes from 10 to 1000
    times = []

    for n in input_sizes:
        s, f = generate_test_case(n)

        # Measure time using perf_counter
        start_time = time.perf_counter()
        printMaxActivities(s, f)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    return input_sizes, times

# Plot the results
def plot_running_time(input_sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times, marker='o', label='Running Time')
    plt.xlabel('Number of Activities (Input Size)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Running Time of Activity Selection Algorithm')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
if __name__ == "__main__":
    input_sizes, times = measure_running_time()
    plot_running_time(input_sizes, times)