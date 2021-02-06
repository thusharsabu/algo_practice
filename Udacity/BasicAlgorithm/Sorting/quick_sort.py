
def quick_sort(arr):
  sort_all(arr, 0, len(arr) - 1)

def sort_all(arr, start, end):
  if end <= start:
    return
  
  pivot = sort_block(arr, start, end)
  sort_all(arr, start, pivot - 1)
  sort_all(arr, pivot + 1, end)

def sort_block(arr, start, end):
  pivot = end
  pivot_value = arr[pivot]

  while pivot > start:
    if pivot_value > arr[start]:
      start += 1
      continue

    if pivot - start == 1:
      arr[pivot], arr[start] = arr[start], arr[pivot]
      pivot -= 1
    else:
      arr[pivot], arr[pivot - 1] = arr[pivot - 1], arr[pivot]
      arr[pivot], arr[start] = arr[start], arr[pivot]
      pivot -= 1
  
  return pivot

items = [8, 3, 1, 7, 0, 10, 2]
quick_sort(items)
print(items)

items = [1, 0]
quick_sort(items)
print(items)

items = [96, 97, 98]
quick_sort(items)
print(items)