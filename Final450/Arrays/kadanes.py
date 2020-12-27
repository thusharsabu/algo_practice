

# Kadane's algo, find maximum sub array

def kadane(arr):
  max_value = arr[0]
  current_total = max_value

  for value in arr[1:]:
    new_total = current_total + value

    current_total = max(new_total, value)
    if current_total > max_value:
      max_value = current_total
  return max_value

print(kadane([1,2,3,-2,5]))