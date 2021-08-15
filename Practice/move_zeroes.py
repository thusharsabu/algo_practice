

# def moveZeros(arr, num):
#   i,j = 0,0
#   arr_len = len(arr)

#   while i < arr_len and j < arr_len:
#     if (arr[j] == num):
#       j += 1
#     elif (arr[i] == num):
#       arr[i], arr[j] = arr[j], arr[i]
#       i += 1
#       j+=1
#     else:
#       i += 1
#       j += 1
  
#   while i  < arr_len:
#     if (arr[i] == num):
#       arr[i] = 0
#     i += 1

def moveZeros(nums, numToBeMoved):

    for i in range(len(nums)):
        if nums[i] == numToBeMoved:
            nums[i] = 0

    l = 0
    r = 0
    zeros = 0
    while r < len(nums):

        if nums[r] == 0:
            zeros += 1
        else:
            nums[l] = nums[r]
            l += 1

        r += 1

    right = len(nums) - 1
    for i in range(zeros):
        nums[right] = 0
        right -= 1

arr = [1,2,3,1,4]
moveZeros(arr, 1)
print(arr)
arr = [5,5,5,5,5,1]
moveZeros(arr, 1)
print(arr)
