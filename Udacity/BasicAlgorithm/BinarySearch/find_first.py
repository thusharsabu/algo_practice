
def find_first(arr, target):
  found = []
  def binary_search(left, right):
    if left > right: return -1

    mid = (left + right) // 2

    if arr[mid] == target:
      found.append(mid)
    
    if arr[mid] >= target:
      right = mid - 1
    else:
      left = mid + 1
    
    return binary_search(left, right)
  binary_search(0, len(arr) - 1)
  return found


print(find_first([1, 3, 5, 7, 7, 7, 8, 11, 12], 7))
print(find_first([1, 7, 7, 7, 7, 8, 8, 9, 10, 11, 12], 7))
print(find_first([1,2,3,4,5,6,7,8,9,10,10,10,10,10], 10))