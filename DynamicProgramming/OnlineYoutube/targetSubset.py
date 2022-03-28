def permutations(target, arr):
    if target == 0:
        return False

    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(target + 1):
        if dp[i]:
            for val in arr:
                if i + val <= target:
                    dp[i + val] = True

    return dp[target]


print(permutations(7, [5, 3, 4, 7]))
print(permutations(7, [2, 4]))
print(permutations(8, [2, 3, 5]))
print(permutations(300, [7, 14]))
