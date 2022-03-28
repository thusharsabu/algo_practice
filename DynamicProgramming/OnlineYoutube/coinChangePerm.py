# Get Permutations of coin changes from given denominations


def coinChange(target, denominations):
    if target == 0:
        return []

    dp = [None] * (target + 1)
    dp[0] = []

    for i in range(target + 1):
        if type(dp[i]) is list:
            for val in denominations:
                if val + i <= target:
                    if dp[val + i] is None:
                        dp[val + i] = []

                    if len(dp[i]) == 0:
                        dp[val + i].append([val])
                    else:
                        for eachComb in dp[i]:
                            eachComb = eachComb[:]
                            dp[val + i].append(eachComb + [val])
    return dp[target]


print(coinChange(7, [2, 3, 5]))
