# Return True if input is palindrome, False otherwise.
# Args:
#     input(str): input to be checked if it is palindrome

# def is_palindrome(input):
#   if len(input) == 0 or len(input) == 1:
#     return True
#   # import pdb; pdb.set_trace()
#   return input[:1] == input[-1] and is_palindrome(input[1:-1])\

def is_palindrome(input):

  def validate(i, j):
    if i >= j:
      return True
    if input[i] != input[j]:
      return False
    i+=1
    j-=1
    return validate(i, j)
  
  return validate(0,len(input) - 1)


print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
