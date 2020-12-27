# You have been given an array of length = n. The array contains integers
# from 0 to n - 2. Each number in the array is present exactly once except for
# one number which is present twice. Find and return this duplicate number
# present in the array

# Example:

# arr = [0, 2, 3, 1, 4, 5, 3]
# output = 3 (because 3 is present twice)
# The expected time complexity for this problem is O(n) and the expected
# space-complexity is O(1).

def duplicate_number(arr):
    len_arr = len(arr)
    expected_total = ((len_arr - 2) * (len_arr-1)) // 2
    current_total = 0
    for value in arr:
        current_total += value
    
    return abs(expected_total - current_total)

# def duplicate_number(arr):
    # len_arr = len(arr)

    # expected_sum = 0
    # current_sum = 0

    # for i in range(len_arr - 1):
    #   expected_sum += i

    # for num in arr:
    #     current_sum += num

    # return current_sum - expected_sum



def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print(output)
        print("Fail")


arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)
