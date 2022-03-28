def howSum(target, arr, mem={}):
    if target < 0:
        return None

    if target == 0:
        return []

    if target in mem:
        return mem[target]

    for value in arr:
        res = howSum(target - value, arr, mem)

        if type(res) is list:
            res.append(value)
            mem[target] = res[:]
            return res

    mem[target] = None
    return mem[target]


def howSum1(target, arr, mem):
    if target == 0:
        return []
    if target < 0:
        return False

    if target in mem:
        return mem[target]

    for val in arr:
        res = howSum(target - val, arr, mem)

        if type(res) is list:
            res.append(val)
            return res

    mem[target] = False
    return False


print(howSum(7, [5, 3, 4, 7], {}))
print(howSum(7, [2, 4], {}))
print(howSum(8, [2, 3, 5], {}))
print(howSum(300, [7, 14], {}))
