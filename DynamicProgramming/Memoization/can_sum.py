def can_sum1(target, arr, mem={}):
    if target == 0:
        return True

    if target < 0:
        return False

    if target in mem:
        return mem[target]

    for value in arr:
        res = can_sum(target - value, arr, mem)

        if res:
            mem[target] = True
            return True
    mem[target] = False
    return False


print(can_sum(7, [5, 3, 4, 7], {}))
print(can_sum(7, [2, 4], {}))
print(can_sum(8, [2, 3, 5], {}))
print(can_sum(300, [7, 14], {}))
