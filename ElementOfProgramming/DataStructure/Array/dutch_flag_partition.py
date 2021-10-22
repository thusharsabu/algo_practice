
def dutch_flag_partition(arr, index):
  pivot = arr[index]

  small = equal = 0
  large = len(arr)

  while equal < large:
    if arr[equal] < pivot:
      arr[small], arr[equal] = arr[equal], arr[small]
      small += 1
      equal += 1
    elif arr[equal] == pivot:
      equal += 1
    else:
      large -= 1
      arr[large], arr[equal] = arr[equal], arr[large]
  return arr

print(dutch_flag_partition([0,1,2,0,2,1,1], 0))
