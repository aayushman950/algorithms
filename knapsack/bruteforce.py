def knapsack_bruteforce(values, weights, capacity):
    n = len(values)
    max_value = 0
    for mask in range(1 << n):
        total_weight = 0
        total_value = 0
        for i in range(n):
            if mask & (1 << i):
                total_weight += weights[i]
                total_value += values[i]
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
    return max_value