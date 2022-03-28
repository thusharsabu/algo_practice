def canConstruct(word, arr, mem={}):
    if word == "":
        return True

    if word in mem:
        return mem[word]

    for value in arr:
        valLen = len(value)

        if len(word) >= valLen and value == word[:valLen]:
            if canConstruct(word[valLen:], arr, mem):

                return True
    mem[word] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    canConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
