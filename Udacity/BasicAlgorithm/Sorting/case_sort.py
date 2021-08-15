# Case Specific Sorting of Strings
# Problem statement
# Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort, that sorts uppercase and lowercase letters separately, such that if the  𝑖 th place in the original string had an uppercase character then it should not have a lowercase character after being sorted and vice versa.

# For example:
# Input: fedRTSersUXJ
# Output: deeJRSfrsTUX

def case_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = case_sort(arr[:mid])
    right = case_sort(arr[mid:])
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
            new_arr.append(left[left_index])
            left_index += 1
        else:
            new_arr.append(right[right_index])
            right_index += 1
    return new_arr + left[left_index:] + right[right_index:]

