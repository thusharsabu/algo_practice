def canSum(target, arr):
    result = [False] * (target + 1)

    result[0] = True

    for i in range(target + 1):
        if result[i] == True:
            for value in arr:
                if value + i < target + 1:
                    result[i + value] = True
    return result[target]


print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))
