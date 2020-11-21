
# Problem Statement

# Given an input string, return all permutations of the string in an array.

# Example 1:

# string = 'ab'
# output = ['ab', 'ba']
# Example 2:

# string = 'abc'
# output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

def permutations(input):
  return return_permutations(input, 0)

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


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)

print(permutations('abc'))