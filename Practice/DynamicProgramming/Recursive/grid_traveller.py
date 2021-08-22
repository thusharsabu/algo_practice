
def grid(m,n, mem = {}):
  if m == 0 or n == 0: return 0
  if m == 1 and n == 1: return 1
  if (m,n) in mem: return mem[(m,n)]

  directions = [(-1, 0), (0, -1)]
  count = 0

  for m1, n1 in directions:
    count += grid(m1+m, n1+n, mem)

  mem[(m,n)] = count
  return mem[(m,n)]


print(grid(2,3)) #3
print(grid(3,3)) #6
print(grid(18,18)) #2333606220

