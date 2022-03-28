def bestSum(target, arr, mem={}):
    if target == 0:
        return []

    if target < 0:
        return None

    if target in mem:
        return mem[target]

    current = []

    for value in arr:
        res = bestSum(target - value, arr, mem)

        if type(res) is list:
            if len(current) > len(res):
                current = res

            current = current[:] + [value]
    mem[target] = None if len(current) == 0 else current

    return mem[target]

print(bestSum(7, [5, 3, 4, 7], {}))
print(bestSum(7, [2, 4], {}))
print(bestSum(8, [2, 3, 5], {}))
print(bestSum(300, [7, 14], {}))
