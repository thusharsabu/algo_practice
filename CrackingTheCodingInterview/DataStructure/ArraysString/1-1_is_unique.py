# Implement an algorithm to determine if a string has all unoque characters. What if you cannot use additional datastructures

# Solutions
# 1. sort and check
# Use dictionary
def unique(str):
  chars = [False for _ in range(128)]
  for value in str:
    if chars[ord(value)] == True:
      return False
    chars[ord(value)] = True
  print(chars)
  return True

print(unique('thushar'))