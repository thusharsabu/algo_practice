

def sort_(arr, begin, end):
  while begin < end:
    if arr[begin] > arr[end]:
      arr[begin], arr[end - 1] = arr[end - 1], arr[begin]
      arr[end], arr[end - 1] = arr[end - 1], arr[end]
      end -= 1
    else:
      begin += 1
  
  return end

def sort_all(arr, begin, end):
  if begin > end:
    return 0
  
  pivot = sort_(arr, begin, end)
  sort_all(arr, begin, pivot - 1)
  sort_all(arr, pivot+1, end)

def quick_sort(arr):
  return sort_all(arr, 0, len(arr) - 1)

arr = [5,4,3,2,1]
quick_sort(arr)
print(arr)

