
def countConstruct(arr, target, mem= {}):
  if target in mem:  return mem[target]
  if target == '': return 1

  count = 0
  for val in arr:
    if len(target) < len(val): continue

    if val == target[:len(val)]:
      count += countConstruct(arr, target[len(val):], mem)
  mem[target] = count
  return count


print(countConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef'))
print(countConstruct(['purp', 'p', 'ur', 'le', 'purpl'], 'purple'))