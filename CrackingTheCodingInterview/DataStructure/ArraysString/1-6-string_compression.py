# String compression aabccccaaa -> a2b1c5a3


def string_compression(str1):
    dict = {}

    current_char = str1[0]
    new_str = ""
    count = 1
    for value in str1[1:]:
        if value == current_char:
            count += 1
        else:
            new_val = current_char + str(count)
            new_str += new_val
            count = 1
            current_char = value

    if len(str1) <= len(new_str):
        return str1
    return new_str

print(string_compression('aabcccccaaa'))
print(string_compression('aabca'))
