
def scatterPalindrome(str1):
  if len(str1) == 0: return 0
  seen = [0] * 26

  for val in str1:
    seen[ord(val) - 97] += 1
  
  odds = 0
  for val in seen:
    if val %2 != 0:
      odds += 1
  
  if odds > 1: return 0
  return 1


# str1 = 'bbrrg'
str1 = 'aabb'
count = 0
for i in range(len(str1)):
  for j in range(len(str1), -1, -1):
    c = scatterPalindrome(str1[i:j])
    count += c
    if c == 1:
      print(str1[i:j])
print(count)


