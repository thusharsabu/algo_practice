
def find_total(arr, total):
  if sum(arr) == total:
    return arr
  else:
    for i in range(len(arr)):
      value = find_total((arr[:i] + arr[i+1:]), total)
      if value is not None:
        return value



print(find_total([200,2,3,4,5,6,7,8,37], 237))