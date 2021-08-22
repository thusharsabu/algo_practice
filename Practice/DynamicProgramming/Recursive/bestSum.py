
def bestSum(arr, target, mem = {}):
  if target == 0: return []
  if target < 0: return None
  if target in mem: return mem[target]

  current = None
  for val in arr:
    remainder = bestSum(arr, target - val, mem)
    if remainder != None:

      new_remainder = remainder[:]
      new_remainder.append(val)
      if current is None or len(new_remainder) < len(current):
        current = new_remainder
        
  mem[target] = current
  return current

print(bestSum([5,3,4,7], 700))
print(bestSum([7,5,3,4], 7000))
# print(mem)


