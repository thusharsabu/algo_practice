# Find square root

def closest_square_root(n):
  start = 0
  end = n//2

  while start <= end:
    mid = (start + end) // 2
    print("Start {}, end {}, mid {}".format(start, end, mid))
    square = mid * mid

    if square == n:
      return mid
    elif square > n:
      end = mid - 1
    else:
      start = mid + 1
  
  return mid

print(closest_square_root(4))