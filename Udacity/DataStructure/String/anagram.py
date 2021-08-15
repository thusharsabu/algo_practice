def anagram_checker1(str1, str2):
    return "".join(sorted(str1.replace(" ", "").lower())) == "".join(
        sorted(str2.replace(" ", "").lower())
    )


def anagram_checker(str1, str2):
    new_str1 = str1.replace(" ", "")
    new_str2 = str2.replace(" ", "")

    char_seq = [0] * 256

    if len(new_str1) != len(new_str2):
        return False

    i = 0

    while i < len(new_str1):

        char_seq[ord(new_str1[i].lower())] += 1
        char_seq[ord(new_str2[i].lower())] -= 1

        i += 1
    for value in char_seq:
        if value != 0:
            return False
    return True


print("Pass" if not (anagram_checker("water", "waiter")) else "Fail")
print("Pass" if anagram_checker("Dormitory", "Dirty room") else "Fail")
print("Pass" if anagram_checker("Slot machines", "Cash lost in me") else "Fail")
print("Pass" if not (anagram_checker("A gentleman", "Elegant men")) else "Fail")
print(
    "Pass"
    if anagram_checker("Time and tide wait for no man", "Notified madman into water")
    else "Fail"
)

print(anagram_checker("Slot machines", "Cash lost in me"))
