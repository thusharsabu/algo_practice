
def palindrome(s, low, hi, seen):
  total = 0
  # print(s)


  while low >= 0 and hi < len(s):
    if s[low:hi] not in seen and s[low] == s[hi]:

      total += 1
      low -= 1
      hi += 1
      print(f"low: {low} and high: {hi}")
      seen.add(s[low:hi])
      # print(s[low:hi])
      # print(seen)
    else:
      return total
  return total

def return_permutations(string, index):
  if index >= len(string):
    return ['']
  else:
    new_string = []
    
    rest_perm = return_permutations(string, index+1)

    current_char = string[index]
    for perm in rest_perm:
      for i in range(0, len(perm) + 1):
        new_char = perm[0:i] + current_char + perm[i:]
        new_string.append(new_char)
      
    return new_string

def permutations(input):
  return return_permutations(input, 0)

def count_palindrome(ss):
  response = []
  for s in ss:
    count = 0
    for str1 in permutations(s):
      seen = set()
      for i in range(len(str1)):
        print(i)
        count += palindrome(s, i, i, seen)
        count += palindrome(s, i, i+1, seen)
    response.append(count)
  return response


print(count_palindrome(['aabb']))
# print(count_palindrome(['bbrrg']))

dict = {}
for (int i = 0; i < lines.length(); i++) {
  for (int j = 0; j < lines[i].length(); j++) {
    if (lines[i][j] == ' ') {
      break;
    }
  }

  
}
