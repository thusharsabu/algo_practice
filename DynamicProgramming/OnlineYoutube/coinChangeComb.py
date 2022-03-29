def coinChange(target, dino):
    if target == 0:
        return []

    dp = [None] * (target + 1)
    dp[0] = []

    for d in dino:
        if dp[d] is None:
            dp[d] = []

        for i in range(target + 1):
            if type(dp[i]) is list and i + d <= target:
                if dp[i + d] is None:
                    dp[i + d] = []

                if len(dp[i]) == 0:
                    dp[d + i].append([d])
                else:
                    for comb in dp[i]:
                        comb = comb[:]
                        dp[i + d].append(comb + [d])

    return dp[target]


print(coinChange(7, [2, 3, 5]))
print(coinChange(8, [2, 3, 5, 4]))
