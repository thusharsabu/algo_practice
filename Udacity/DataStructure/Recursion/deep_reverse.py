# Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the
# deep reverse of the input list.
# This means it reverses all the elements in the list, and if any of those elements are lists themselves,
# reverses all the elements in the inner list, all the way down.

# Note: The procedure must not change the input list itself.

# def deep_reverse(l):
#     if len(l) == 1 and type(l[0]) is not list:
#         return l
#     import pdb; pdb.set_trace()
#     return deep_reverse(l[1:]) + l[:1] if type(l[:1][0]) is not list else deep_reverse(l[:1][0])


def deep_reverse(arr):
    if len(arr) <= 1:
        return arr
    current = arr[:1]
    rest = deep_reverse(arr[1:])
    if isinstance(current, list):
        current = deep_reverse(current)
    
    return rest + current

print(deep_reverse([1, 2, 4]))
print(deep_reverse([[2, 4], 1]))
