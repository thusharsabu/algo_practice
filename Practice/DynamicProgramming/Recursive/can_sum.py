
def canSum(arr, target, mem = {}):
  if target == 0: return True
  if target < 0: return False
  if target in mem: return mem[target]

  for val in arr:
    if canSum(arr, target - val):
      return True
  
  mem[target] = False
  return False


print(canSum([7,14], 300))