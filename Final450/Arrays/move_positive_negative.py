# Move all negative numbers to beginning and positive to end with constant extra space
# Last Updated: 07-11-2020
# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all
# negative numbers appear before all positive numbers.
# Examples :

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


# Note: Order of elements is not important here.


def rearrange(arr):
    j = len(arr) - 1
    # rearranged = True

    for i in range(len(arr)):
      if arr[i] >= 0:
        while j > i:
          if arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
            break
          else:
            j -= 1
        if j <= i:
          return arr
    return arr      




print(rearrange([1, 2, -1, 4, -5, 7, 8, 9, -10, 4]))
print(rearrange([-1,-2, -4, 6, -7, 1]))
