# Problem Statement
# Given an integer array, find and return all the subsets of the array. The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

# Note:

# An empty set will be represented by an empty list.
# If there are repeat integers, each occurrence must be treated as a separate entity.
# Example 1

# arr = [9, 9]

# output = [[],
#           [9],
#           [9],
#           [9, 9]]
# Example 2

# arr = [9, 12, 15]

# output =  [[],
#            [15],
#            [12],
#            [12, 15],
#            [9],
#            [9, 15],
#            [9, 12],
#            [9, 12, 15]]


def subsets(arr):
    def find_subsets(new_arr, new_list):

        if len(new_arr) == 0:
            return
        new_list.append(new_arr[:])
        len_arr = len(new_arr)
        for val in range(len_arr):
            new_arr_ = new_arr[(val + 1):]

            find_subsets(new_arr_, new_list)

        return new_list

    return find_subsets(arr[:], [])


print(subsets([9, 12, 15]))
