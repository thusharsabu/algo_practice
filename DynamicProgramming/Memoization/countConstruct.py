def countConstruct(word, arr, mem={}):
    if word == "":
        return 1
    if word in mem:
        return mem[word]

    count = 0

    for val in arr:
        valLen = len(val)

        if val == word[:valLen]:
            count += countConstruct(word[valLen:], arr, mem)
    mem[word] = count
    return count


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))
print(
    countConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        {},
    )
)
