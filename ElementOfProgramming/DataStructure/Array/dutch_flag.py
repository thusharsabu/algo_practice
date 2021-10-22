

def dutch_flag(arr, pivotIn):
  pivot = arr[pivotIn]

  smaller = 0
  for i in range(len(arr)):
    if arr[i] < pivot:
      arr[i], arr[smaller] = arr[smaller], arr[i]
      smaller += 1
  
  larger = len(arr) - 1

  for i in reversed(range(len(arr))):
    print(arr[i])
    if arr[i] > pivot: break
    if arr[i] > pivot:
      print('larger')
      arr[i], arr[larger] = arr[larger], arr[i]
      larger -= 1
  return arr

print(dutch_flag([0,1,2,0,2,1,1], 2))
