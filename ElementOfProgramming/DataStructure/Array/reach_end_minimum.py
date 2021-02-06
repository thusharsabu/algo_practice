
def can_reach_end(arr, count):
  if len(arr) <= 1:
    return 1
  found_path = False
  
  if arr[0] > 0:
    # count += 1
    current_counts = []
    for i in reversed(range(arr[0])):
      value = can_reach_end(arr[i+1:], 1)
      if value:
        # print("The index is {}, the value is: {} and Arr is: {}".format(i, value, arr))

        found_path = True
        current_counts.append(value)
        if value == 1:
          return 2
  if found_path:
    print(current_counts)
    return (1 + min(current_counts))
  else:
    return False


print(can_reach_end([1,1,1,1,1,1], 0))