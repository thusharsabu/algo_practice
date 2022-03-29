def knapsack(cap, weights, values):
    dp = [0] * (cap + 1)

    for i in range(cap + 1):
        for j in range(len(weights)):
            if weights[j] <= i:
                dp[i] = max(dp[i], values[j] + dp[i - weights[j]])
                print(dp)
    print(dp)asdasdas


print(
    knapsack(
        7,
        [2, 5, 1, 3, 4],
        [15, 14, 10, 45, 30],
    )
)
