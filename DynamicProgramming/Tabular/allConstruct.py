def allConstruct(word, arr):
    if word == "":
        return []

    result = []
    wordLen = len(word)
    table = [None] * (wordLen + 1)

    table[0] = []

    for i in range(wordLen + 1):
        if type(table[i]) is list:
            for value in arr:
                valLen = len(value)

                if valLen + i <= wordLen and value == word[i : i + valLen]:
                    current = table[i + valLen]

                    if current is None:
                        table[i + valLen] = []

                    if len(table[i]) == 0:
                        table[i + valLen].append([value])
                    else:
                        for comb in table[i]:
                            table[i + valLen].append(comb[:] + [value])
    return table[wordLen]


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    allConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
