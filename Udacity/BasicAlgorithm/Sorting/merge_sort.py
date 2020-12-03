# Implement Merge Sort


def merge(left, right):
    if left is None:
        if right is None:
            return []
        else:
            return right
    elif right is None:
        return left

    left_index = right_index = 0
    merged = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += right[right_index:]
    merged += left[left_index:]
    return merged


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    len_arr = len(arr)
    mid_point = len_arr // 2

    left = merge_sort(arr[:mid_point])
    right = merge_sort(arr[mid_point:])

    return merge(left, right)


print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2]))
