
def rearrange(arr):
  for i in range(len(arr)):
    arr[i:i+2] = sorted(arr[i:i+2], reverse=i%2)
    print("SOrted: {}".format(sorted(arr[i:i+2], reverse=i%2)))
    print(arr)
    print('-----')
  return arr

print(rearrange([1,2,3,8,4,5,6]))
print(rearrange([8,9,5,1,2,4,0,88]))
