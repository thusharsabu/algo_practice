
def allConstruct(arr, target, mem= {}):
  if target == '': return [[]]
  print(target)
  
  result = []
  for val in arr:
    if len(val) <= len(target) and val == target[:len(val)]:
      value = allConstruct(arr, target[len(val):], mem)

      if value != None:
        for eachSet in value:
          result.append([val]+eachSet)
  mem[target] = result
  return None if len(result) == 0 else result


print(allConstruct(['purp', 'p', 'ur', 'le', 'purpl'], 'purple'))