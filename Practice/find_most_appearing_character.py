
def fin_char(str_arr):
  count = {}

  for word in str_arr:
    current_unique = {}
    for char in word:
      if char not in current_unique:
        if char in count:
          count[char] += 1
        else:
          count[char] = 1
        current_unique[char] = 1
  new_arr = []
  len_arr = len(str_arr)

  for key in count:
    if count[key] == len_arr:
      new_arr.append(key)
  
  return new_arr


print(fin_char(['cat', 'boat', 'rat']))
