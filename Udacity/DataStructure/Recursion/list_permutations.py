# Given a list of items, the goal is to find all of the permutations of that list. For example,
# if given a list like: ["apple", "water"], you could create two permuations from it.
# One in the form of the original input and one in the reversed order like so: ["water","apple"]

# Return a list of permutations
# Examples:
#     permute([0, 1]) returns [ [0, 1], [1, 0] ]
# Args:
#   l(list): list of items to be permuted
# Returns:
#   list of permutation with each permuted item be represented by a list

import copy

# def permute(l):
#   new_list = []

#   if len(l) == 0:
#     new_list.append([])
#   else:
#     first_ele = l[0]
#     rest_ele = permute(l[1:])

#     for each_ele in rest_ele:
#       for i in range(0, len(each_ele)+1):
#         each_ele_new = copy.deepcopy(each_ele)
#         each_ele_new.insert(i, first_ele)
#         new_list.append(each_ele_new)
    
#   return new_list

def permute(l):

  new_arr = []
  if len(l) == 0:
    new_arr.append([])
    return new_arr

  current = l[0]
  remaining = permute(l[1:])

  for each_ele in remaining:
    for i in range(len(each_ele) + 1):
      ins = copy.deepcopy(each_ele)
      ins.insert(i, current)
      new_arr.append(ins)
  return new_arr


def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True
    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e



print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")