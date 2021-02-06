# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word
# or a phrase that is the same forwards and backwards. A permutation ia a rerrangement of letters. The palindrome does not need to be 
# limited to just dictionary.


def palindrome_permutation(str):
  dict = {}
  ones = 0
  str = str.lower()

  for value in str:
    if value != ' ':
      if value in dict:
        dict[value] += 1
      else:
        dict[value] = 1
  
  for k, v in dict.items():
    if v % 2 != 0:
      if ones != 0:
        return False
      ones = 1
  return True

print(palindrome_permutation('madazm'))