def countConstruct(word, arr):
    count = 0
    if word == "":
        return count
    wordLen = len(word)
    result = [0] * (wordLen + 1)
    result[0] = 1

    for i in range(len(result)):
        if result[i]:
            for value in arr:
                valLen = len(value)

                if i + valLen <= wordLen and value == word[i : i + valLen]:
                    result[i + valLen] += result[i]

    return result[wordLen]


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    countConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
