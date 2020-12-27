# Given two arrays A and B of size N and M respectively. The task is to find union between these
# two arrays.
# Union of the two arrays can be defined as the set containing distinct elements from both
# the arrays.
# If there are repetitions, then only one occurrence of element should be printed in union.


def find_union(arr1, arr2):
    if len(arr1) < len(arr2):
        return find_union1(arr1, arr2)
    else:
        return find_union1(arr2, arr1)


def find_union1(small, large):
    small.sort()
    new_arr = []
    for value in large:
        print("The Array is: " + str(small))
        print("The value is: " + str(value))
        output = binary_search(small, value)
        if output:
            new_arr.append(output)
    return new_arr


def binary_search(arr, value):
    if len(arr) is 0:
        return False
    mid = len(arr) // 2
    if arr[mid] == value:
        return arr[mid]

    if value < arr[mid]:
        return binary_search(arr[:(mid)], value)
    else:
        return binary_search(arr[mid+1:], value)


print("The sol is: " + str(find_union([7, 1, 5, 2, 3, 6], [3, 8, 6, 20, 7])))
