#User function Template for python3

def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    if k > len(arr):
        return
    a = merge_sort(arr)
    print(a)
    print(k)
    return a[k - 1]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    
    if len(left) == 0:
        return right
    elif len(right) < 0:
        return left
    
    i =j = 0
    new_arr = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1
        
    new_arr += left[i:]
    new_arr += right[j:]
    return new_arr

print(kthSmallest([7, 10, 4, 3, 20, 15], 0,0, 3))
print(kthSmallest([7, 10, 4, 20, 15], 0,0, 4))
