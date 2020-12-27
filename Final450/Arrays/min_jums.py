# Given an array of integers where each element represents the max number of steps that can be
# made forward from that element. Write a function to return the minimum number of jumps to
# reach the end of the array (starting from the first element). If an element is 0, then cannot
# move through that element.


def min_jumps(arr):

    if arr[0] <= 0:
        return -1

    if len(arr)-1 <= arr[0]:
        return 1
    current_lengths = []
    for i in range(arr[0]):
        a = min_jumps(arr[arr[0] - i:])
        if a != -1:
            current_lengths.append(a + 1)
            return a + 1
    return -1


# print(min_jumps([1, 4, 3, 2, 6, 7]))
# print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(min_jumps([5,9,3,2,1,0,2,3,3,1,0,0]))