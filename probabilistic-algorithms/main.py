import time
import matplotlib.pyplot as plt
from lasvegas import lasvegas_nqueens
from montecarlo import montecarlo_nqueens

def measure_performance(algorithm, n, trials=10):
    successes = 0
    total_time = 0
    for _ in range(trials):
        start = time.perf_counter()
        result = algorithm(n)
        elapsed = time.perf_counter() - start
        total_time += elapsed
        if result is not None:
            successes += 1
    success_rate = (successes / trials) * 100
    avg_time = total_time / trials
    return success_rate, avg_time

def main():
    n_values = list(range(4, 16))  # Test for N=4 to N=15
    lasvegas_success = []
    lasvegas_times = []
    montecarlo_success = []
    montecarlo_times = []

    for n in n_values:
        # Las Vegas
        lv_rate, lv_time = measure_performance(lasvegas_nqueens, n)
        lasvegas_success.append(lv_rate)
        lasvegas_times.append(lv_time)
        
        # Monte Carlo
        mc_rate, mc_time = measure_performance(montecarlo_nqueens, n)
        montecarlo_success.append(mc_rate)
        montecarlo_times.append(mc_time)

    # Plot success rates
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(n_values, lasvegas_success, 'bo-', label='Las Vegas')
    plt.plot(n_values, montecarlo_success, 'ro-', label='Monte Carlo')
    plt.xlabel('Number of Queens (N)')
    plt.ylabel('Success Rate (%)')
    plt.title('Success Rate Comparison')
    plt.legend()

    # Plot time efficiency
    plt.subplot(1, 2, 2)
    plt.plot(n_values, lasvegas_times, 'bo-', label='Las Vegas')
    plt.plot(n_values, montecarlo_times, 'ro-', label='Monte Carlo')
    plt.xlabel('Number of Queens (N)')
    plt.ylabel('Average Time (seconds)')
    plt.title('Time Efficiency Comparison')
    plt.legend()

    plt.tight_layout()
    plt.savefig('nqueens_comparison.png')
    plt.show()

if __name__ == "__main__":
    main()