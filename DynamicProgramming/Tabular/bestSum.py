def bestSum(target, arr):
    if target == 0:
        return None

    result = [None] * (target + 1)
    result[0] = []

    for i in range(target + 1):
        if result[i] is not None:
            current = result[i]

            for value in arr:
                if value + i <= target:
                    if (
                        result[value + i] is None
                        or len(result[value + i]) > len(result[i]) + 1
                    ):
                        result[value + i] = current[:] + [value]

    return result[target]


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(7, [2, 4]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(300, [7, 14]))
