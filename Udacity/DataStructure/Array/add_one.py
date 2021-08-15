# You are given a non-negative number in the form of list elements. For example, the number 123
# would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form
# of a new list.

# Example 1:

# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:

# input = [9, 9, 9]
# output = [1, 0, 0, 0]


def add_one1(arr, borrow):
    arr_len = len(arr) - 1

    while arr_len != -1:
        add_value = arr[arr_len] + borrow
        if add_value % 10 == 0:
            arr[arr_len] = 0
            arr_len -= 1
        else:
            arr[arr_len] = add_value
            return arr

    return [1] + arr

def add_one(arr, borrow):    
    for i in range(len(arr) - 1, -1, -1):
        if borrow == 0:
            break
        if (arr[i] + borrow) > 9:
            arr[i] = 0
        else:
            arr[i] = arr[i] + borrow
            return arr
    return [1] + arr


print(add_one([0], 1))
print(add_one([1, 0], 1))
print(add_one([9, 9, 9, 9], 1))
print(add_one([9, 8, 9, 9], 1))
