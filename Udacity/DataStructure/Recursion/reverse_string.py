
# Return reversed input string
# Examples:
#     reverse_string("abc") returns "cba"
# Args:
#   input(str): string to be reversed
# Returns:
#   a string that is the reverse of input

def reverse_string(str_value):
  if len(str_value) <= 1:
    return str_value
  
  return reverse_string(str_value[1:]) + str_value[:1]


print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
