def canConstruct(word, arr):
    if word == "":
        return False

    result = [False] * (len(word) + 1)
    result[0] = True

    for i in range(len(word)):
        current = word[i]

        for value in arr:
            if result[i] and value[0] == current:
                index = i
                j = 0
                similar = True
                while j < len(value) and i + j + 1 <= len(word):
                    if value[j] != word[i + j]:
                        similar = False
                        break
                    j += 1

                if similar:
                    result[i + j] = True
    return result[len(word)]


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    canConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
