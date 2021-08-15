

def word_flipper(our_string):    
  new_arr = our_string.split(' ')
  for i in range(len(new_arr)):
      new_arr[i] = new_arr[i][::-1]
  
  return ' '.join(new_arr)

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")