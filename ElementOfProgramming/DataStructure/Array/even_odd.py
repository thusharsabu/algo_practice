# Move all even to left and odd to left

def even_odd(arr):
  # for i in range(len(arr)):
  even = []
  odd = []
  for value in arr:
    if value % 2 == 0:
      even.append(value)
    else:
      odd.append(value)
  return even + odd

print(even_odd([1,2,3,4,5,6,7,8,10]))

def even_odd_in_place(arr):
  even, odd = 0, len(arr) - 1

  while even < odd:
    if arr[even] % 2 == 0:
      even += 1
    else:
      arr[even], arr[odd] = arr[odd], arr[even]
      odd -= 1

  return arr

print(even_odd_in_place([1,2,3,4,5,6,7,8,10]))
  