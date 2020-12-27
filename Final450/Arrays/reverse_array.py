# Write a program to reverse an array or string


def reverse_array_recursion(arr):
    if len(arr) == 0:
        return []
    else:
        return reverse_array_recursion(arr[1:]) + arr[:1]


# print(reverse_array_recursion([1, 2, 3]))
# print(reverse_array_recursion([4, 5, 1, 2]))


def reverse_array(arr):
    length = len(arr) - 1

    for i in range(length + 1):
        print("The i value is " + str(i))
        print("the length value is: " + str(length - i))
        if i >= (length - i):
            return arr
        else:
            temp = arr[i]
            arr[i] = arr[length - i]
            arr[length - i] = temp


# print(reverse_array([1, 2, 3]))
print(reverse_array([4, 5, 1, 2]))
# def reverse_string(str_value):
#     if len(str_value) <= 1:
#         return str_value

#     return reverse_string(str_value[1:]) + str_value[:1]


def reverse_string(str):
    if len(str) <= 1:
        return str
    else:
        return reverse_string(str[1:]) + str[:1]


print(reverse_string("hello"))
