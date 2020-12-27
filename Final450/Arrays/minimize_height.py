# Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer.
# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.


def get_min_diff(arr, k):
    median = sum(arr) // len(arr)
    if arr[0] < median:
      arr[0] = arr[0] + k
    else:
      arr[0] = arr[0] - k
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < median:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i] - k

        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]     
    return max - abs(min)


print(get_min_diff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 5))