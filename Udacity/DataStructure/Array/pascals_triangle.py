# Problem Statement
# Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

# For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

# To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html

def nth_row(n):
  if n == 0:
    return [1]
  else:
    return get_triangle(n-1, [1])

def get_triangle(n, arr):
  if n < 0:
    return arr
  else:
    new_arr = []
    for i in range(len(arr) - 1):
      new_arr.append(arr[i] + arr[i+1])
    return get_triangle(n-1, [1] + new_arr + [1])

print(nth_row(0)) #[1,1]
print(nth_row(1)) #[1,1]
print(nth_row(2))
print(nth_row(3))
print(nth_row(4))# Should return [1, 4, 6, 4, 1]
print(nth_row(5)) # should return [1, 5, 10, 10, 5, 1]


