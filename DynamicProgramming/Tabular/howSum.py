def howSum1(target, arr):
    if target == 0:
        return []

    result = [None for i in range(target + 1)]

    result[0] = []

    for i in range(target + 1):
        if type(result[i]) is list:

            for value in arr:
                if value + i <= target:
                    result[i + value] = result[i] + [value]

    return result[target]


def howSum(target, arr):
    dp = [None] * (target + 1)

    dp[0] = []

    for i in range(target + 1):
        if type(dp[i]) is list:
            for val in arr:
                if i + val <= target:
                    dp[i + val] = dp[i] + [val]
    return dp[target]


print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))
