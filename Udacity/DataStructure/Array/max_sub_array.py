# Problem Statement
# You have been given an array containg numbers. Find and return the largest sum in a contiguous
# subarray within the input array.

# Example 1:

# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.
# Example 2:

# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.

def max_sub_array(arr):
  max_value = current_value = arr[0] 

  for value in arr[1:]:
    current_value += value

    current_value = max(value, current_value)

    if current_value > max_value:
      max_value = current_value
  
  return max_value


print(max_sub_array([1, 2, 3, -4, 6]))
print(max_sub_array([1, 2, -5, -4, 1, 6]))
