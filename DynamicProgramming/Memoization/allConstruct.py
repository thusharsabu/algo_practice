def allConstruct1(word, arr, mem={}):
    if word == "":
        return [[]]

    if word in mem:
        return mem[word]

    result = []

    for val in arr:
        valLen = len(val)

        if val == word[:valLen]:
            res = allConstruct(word[valLen:], arr)

            for comb in res:
                newRes = comb[:] + [val]
                result.append(newRes)
    mem[word] = result
    return result


def allConstruct2(word, arr, mem={}):
    if word == "":
        return [[]]

    if word in mem:
        return mem[word]

    result = []

    for value in arr:
        if value == word[: len(value)]:
            ways = allConstruct(word[len(value) :], arr, mem)

            for way in ways:
                result.append(way[:] + [value])

    mem[word] = result
    return result


def allConstruct(word, arr, mem):
    print(word)
    if word == "":
        return [[]]

    if word in mem:
        return mem[word]

    result = []

    for val in arr:
        valLen = len(val)

        if val == word[:valLen]:
            res = allConstruct(word[valLen:], arr, mem)

            for eachRes in res:
                eachRes = eachRes[:]
                eachRes.append(val)
                result.append(eachRes)
    mem[word] = result[:]
    return mem[word]


# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
# print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))
print(
    allConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeez",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        {},
    )
)
