

def incrementer(start, end):
  if start is end:
    return 0
  if start > end:
    return -1
  else:
    return 1


arr = [[0 for i in range(20)] for j in range(20)]

def print_line():
  for i in range(20):
    for j in range(20):
      print(arr[i][j], end='')
    print()

def draw_line(startx, starty, endx, endy):
  x_incrementer = incrementer(startx, endx)
  y_incrementer = incrementer(starty, endy)

  arr[startx][starty] = 1
  current_x = startx
  current_y = starty
  print(f"x incrementer is: {x_incrementer} and y incrementer is: {y_incrementer}")
  while current_x != endx or current_y != endy:
    if current_x != endx:
      current_x += x_incrementer
    
    if current_y != endy:
      current_y += y_incrementer
    
    arr[current_x][current_y] = 1

# initialize_array()
# draw_line(0,0,19,19)
# print_line()

# draw_line(0,0,0,18)
# print_line()

# draw_line(19, 0, 0,19)
# print_line()

# draw_line(19, 0, 0,19)
# print_line()

# draw_line(15,0, 15,19)
# print_line()

draw_line(19,0, 0,19)
print_line()

