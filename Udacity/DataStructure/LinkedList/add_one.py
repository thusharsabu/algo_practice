# Problem Statement¶
# You are given a non-negative number in the form of list elements. For example, the number 123
# would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a
# new list.

# Example 1:

# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:

# input = [9, 9, 9]
# output = [1, 0, 0, 0]

# def add_one(arr):
#   carry = 1
#   len_arr = len(arr)
#   last_index = len_arr - 1
#   for index in range(len_arr):
#     total = arr[last_index - index] + carry
#     carry = 0
#     if total >= 10:
#       carry = 1
#       arr[last_index - index] = total % 10
#     else:
#       arr[last_index - index] = total

#   if carry == 0:
#     return arr
#   else:
#     return [1] + arr

def add_one(arr):
  carry = 1

  for index in range(len(arr)-1, -1, -1):
    total = arr[index] + carry

    if total > 9:
      arr[index] = total % 10
      carry = total //10
    else:
      arr[index] = total
      return arr
  return [carry] + arr
  

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

arr = [0]
print(add_one(arr))
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
print(add_one(arr))
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
print(add_one(arr))
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)


