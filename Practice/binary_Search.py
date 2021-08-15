# Binary search

def search(arr, value):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == value:
      return mid
    
    if arr[mid] > value:
      right = mid - 1
    else:
      left = mid + 1


print(search([1,2,3,4,5,78,99,456], 1))
