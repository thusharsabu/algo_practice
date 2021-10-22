

# def multiply(arr1, arr2):
#   result = [0] * (len(arr1) + len(arr2))

#   for i in reversed(range(len(arr1))):
#     for j in reversed(range(len(arr2))):
#       result[i + j + 1] += arr2[j] * arr1[i]
#       # print("The mul is: {}".format(result[i+j+1]))
#       if result[i+j+1] >= 10:
#         result[i+j] += result[i+j+1] // 10
#         result[i+j+1] = result[i+j+1] % 10
#         # print("The value of i is: {} and j is: {}".format(i, j))
#         # print(result)
#         # print("-------------------")
  
#   i = 0
#   while result[i] == 0:
#     i += 1
#   return result[i:]

def multiply(arr1, arr2):
  result = [0]


print(multiply([1,1], [1,1]))
print(multiply([9,9], [8,8]))
print(multiply([1,1], [1]))
