# def string_reverser(str1):
#   return str1[::-1]


def string_reverser1(str1):
    len_arr = len(str1)
    arr = [0] * len_arr

    start = 0
    end = len_arr - 1

    while start <= end:
        if start == end:
            arr[start] = str1[start]
        arr[start] = str1[end]
        arr[end] = str1[start]

        start += 1
        end -= 1
    return "".join(arr)


def string_reverser(str1):
    len_str = len(str1)
    new_str = [0] * (len_str)

    start = 0
    end = len_str - 1
    while start <= end:
        if start == end:
          new_str[start] = str1[start]
        else:
          new_str[start], new_str[end] = str1[end], str1[start]
        start += 1
        end -= 1
    return "".join(new_str)


print(string_reverser("thushar"))
print(string_reverser("water"))
print("Pass" if ("retaw" == string_reverser("water")) else "Fail")
print(
    "Pass"
    if (
        "!noitalupinam gnirts gnicitcarP"
        == string_reverser("Practicing string manipulation!")
    )
    else "Fail"
)
print(
    "Pass"
    if ("3432 :si edoc esuoh ehT" == string_reverser("The house code is: 2343"))
    else "Fail"
)
