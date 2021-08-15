def perm(newArr):
    n = len(newArr)
    curArr = [0] * len(newArr)

    for i in range(len(newArr)):
        if i % 2 == 0:
            curArr[i] = newArr[i // 2]
        else:
            curArr[i] = newArr[n // 2 + (i - 1) // 2]
    return curArr


def reinitializePermutation(n):
    newArr = []
    for i in range(n):
        newArr.append(i)
    count = 1
    permArr = newArr
    isEqual = False
    while not isEqual:
        newPerm = perm(permArr)
        print(newPerm)
        if newArr == newPerm:
            return count
        permArr = newPerm
        count += 1


print(reinitializePermutation(2))

print(reinitializePermutation(4))
