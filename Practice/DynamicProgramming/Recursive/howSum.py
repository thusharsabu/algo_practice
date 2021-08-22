
def howSum(arr, target, mem = {}):
  if target ==0: return []
  if target < 0: return None

  if target in mem: return mem[target]

  for val in arr:
    res = howSum(arr, target - val, mem)
    # if isinstance(res, list):
    if res != None:
      res.append(val)
      return res
  
  mem[target] = None
  return None

print(howSum([5,3,4,7], 7))

