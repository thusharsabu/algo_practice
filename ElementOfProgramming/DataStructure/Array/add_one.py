

def add_one(arr):
  carry = 1
  for i in reversed(range(len(arr))):
    total = arr[i] + carry

    if total >= 10:
      arr[i] = total % 10
      carry = 1
    else:
      arr[i] = total
      carry = 0
  
  if carry > 0:
    return [carry] + arr
  return arr



print(add_one([9,9,9,9]))
print(add_one([1,2,9]))