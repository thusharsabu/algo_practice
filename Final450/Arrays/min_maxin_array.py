# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/


def min_max(arr):
    min = max = arr[0]

    for ele in arr[1:]:
        if ele > max:
            max = ele
        elif ele < min:
            min = ele
    return [min, max]


print(min_max([3, 1, 2, 4, 0, 5, 69, 6, 8, 9]))
