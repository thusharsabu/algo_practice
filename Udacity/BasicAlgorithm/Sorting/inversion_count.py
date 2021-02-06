# Counting Inversions
# The number of inversions in a disordered list is the number of pairs of elements that are
# inverted (out of order) in the list.

# Here are some examples:

# [0,1] has 0 inversions
# [2,1] has 1 inversion (2,1)
# [3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
# [7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
# The number of inversions can also be thought of in the following manner.

# Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j,
# if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.


# def merge(left, right, count):
#     if left is None:
#         if right is None:
#             return []
#         else:
#             return [right, count]
#     elif right is None:
#         return [left, count]

#     left_index = right_index = 0
#     merged = []

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             count += 1
#             merged.append(right[right_index])
#             right_index += 1

#     merged += right[right_index:]
#     merged += left[left_index:]
#     return [merged, count]


# def merge_sort(arr, count):
#     if len(arr) == 1:
#         return [arr, count]

#     len_arr = len(arr)
#     mid_point = len_arr // 2

#     left, count = merge_sort(arr[:mid_point], count)
#     right, count = merge_sort(arr[mid_point:], count)

#     return merge(left, right, count)


def merge_sort(arr, inversion):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    if left == None or len(left) == 0:
        return right
    elif right == None or len(right) == 0:
        return left
    left_index = right_index = 0
    new_arr = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new_arr.append()
            left_index += 1
        else:
            new_arr.append(right[right_index])
            right_index += 1
    return new_arr + left[left_index:] + right[right_index:]


# print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2], 0))
print(merge_sort([7, 5, 3, 1], 0))
