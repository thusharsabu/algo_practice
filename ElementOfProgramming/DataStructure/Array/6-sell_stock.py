# 5.6

def stock(arr):
  max_value = 0
  current = arr[0]
  for value in arr[1:]:
    if current > value:
      current = value
    else:
      max_value = max(max_value, value - current)
  
  return max_value


print(stock([310,315, 275, 295, 260, 270, 290, 230, 255, 250]))
