def knapsack_bottom_up(values, weights, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]