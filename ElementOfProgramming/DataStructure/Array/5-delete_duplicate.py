
def delete_duplicate(arr):
  current = arr[0]
  j = 1
  for i in range(1, len(arr) - 1):
    if j > len(arr) - 1:
      j = i
      break
    while arr[j] == current:
      j += 1
    arr[i] = arr[j]
    current = arr[i]
    j += 1
  for j in range(j, len(arr)):
    arr[j] = 0
  print(arr)


delete_duplicate([2,3,5,5,7,11,11,11,13])