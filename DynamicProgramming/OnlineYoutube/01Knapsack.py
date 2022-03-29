def knapsack(k, weights, values):
    if k == 0:
        return 0

    dp = [[0 for _ in range(k + 1)] for _ in range(len(weights) + 1)]

    for i in range(1, len(weights) + 1):
        for j in range(k + 1):
            if j < weights[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]]
                )

    return dp[len(weights)][k]


print(
    knapsack(
        7,
        [2, 5, 1, 3, 4],
        [15, 14, 10, 45, 30],
    )
)
