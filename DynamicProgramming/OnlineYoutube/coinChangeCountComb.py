def coinChange(target, dino):
    if target == 0:
        return []

    dp = [0] * (target + 1)
    dp[0] = 1

    for d in dino:
        for i in range(d, target + 1):
            if d <= target:
                dp[i] += dp[i - d]
    return dp[target]


print(coinChange(7, [2, 3, 5]))
print(coinChange(8, [2, 3, 5, 4]))
