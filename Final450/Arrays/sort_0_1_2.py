# Sort an array of 0s, 1s and 2s
def sort012(arr,n):
    # code here
    left = []
    mid = []
    right = []
    
    for value in arr:
        if value == 0:
            left.append(value)
        elif value == 1:
            mid.append(value)
        else:
            right.append(value)
    return left + mid + right

print(sort012([0,1,0,2,0,1,0,2,0], 4))