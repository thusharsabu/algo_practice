# Cyclically rotate an array by one

def rotate(arr):
  last = arr[-1]
  len_arr = len(arr)
  j = len_arr - 1
  for _ in range(1, len_arr):
    arr[j] = arr[j - 1]
    j -= 1
  arr[0] = last
  return arr

print(rotate([1,2,3,4,5]))

