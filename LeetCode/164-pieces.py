def canFormArray(arr, pieces):
    n = len(arr)
    i = 0
    while i < n:
        # find target piece
        for p in pieces:
            if p[0] == arr[i]:
                break
        else:
            print('reached')
            return False
        # check target piece
        # python saves the last iterated `p`
        for x in p:
            if x != arr[i]:
                return False
            i += 1
    return True

print(canFormArray([15, 88], [[81],[15]]))
