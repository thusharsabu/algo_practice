
def canConstruct(arr, target, mem = {}):
  if target == '': return True
  if target in mem: return mem[target]

  for value in arr:
    if len(value) > len(target): continue

    i = 0
    substring = True
    while i < len(value):

      if value[i] != target[i]:
        substring = False
        break
      i += 1
    
    if substring and canConstruct(arr, target[i:]): return True
  mem[target] = False
  return False

print(canConstruct(['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], 'skateboard'))
print(canConstruct(['e', 'ee', 'eeeee', 'eee', 'eeee', 'eeeeee', 'eeeeee', 'e'], 'eeeeeeeeeeeeeeeeeeeeeeeeeeeef'))


