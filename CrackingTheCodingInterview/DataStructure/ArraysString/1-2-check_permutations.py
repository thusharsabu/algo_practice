# Given two strings write a method to decide if one is a permutation of the other.

# 1. sort and compare 
# 2. dict and compare
# 3. n square  

def is_subset(str1, str2):
  if len(str1) != len(str2):
    return False

  dict = {}
  for char in str1:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1

  for char in str2:
    if char in dict:
      dict[char] -= 1
      if dict[char] < 0:
        return False
    else:
      return False
  return True


print(is_subset('thushar', 'rahsuht'))
print(is_subset('thushar', 'rahsuh'))