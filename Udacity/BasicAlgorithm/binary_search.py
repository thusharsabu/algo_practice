# Binary search practice
# Let's get some practice doing binary search on an array of integers. We'll solve the problem two different ways—both iteratively and resursively.

# Here is a reminder of how the algorithm works:

# Find the center of the list (try setting an upper and lower bound to find the center)
# Check to see if the element at the center is your target.
# If it is, return the index.
# If not, is the target greater or less than that element?
# If greater, move the lower bound to just above the current center
# If less, move the upper bound to just below the current center
# Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
# Problem statement:
# Given a sorted array of integers, and a target value, find the index of the target value in the array. If the target value is not present in the array, return -1.

# Iterative solution


def binary_search_iterative(array, target):
    if array is None or len(array) == 0:
        return None

    arr_len = len(array)
    start = 0
    end = arr_len
    mid = arr_len // 2

    while start < mid:
        middle = array[mid]
        print("Middle: " + str(middle))
        if middle == target:
            return middle

        if middle > target:
            end = mid
        else:
            start = mid

        mid = (start + end) // 2


# def test_function(test_case):
#     answer = binary_search_iterative(test_case[0], test_case[1])
#     print(answer)
#     if answer == test_case[2]:
#         print("Pass!")
#     else:
#         print("Fail!")


# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 6
# index = 6
# test_case = [array, target, index]
# test_function(test_case)


def binary_search_recursive(array, target):
    if len(array) <= 0 or array is None or target is None:
        return None

    start = 0
    end = len(array)
    mid = (start + end) // 2

    if array[mid] == target:
        return array[mid]

    if array[mid] > target:
        return binary_search_recursive(array[:mid], target)
    else:
        return binary_search_recursive(array[mid:], target)


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)