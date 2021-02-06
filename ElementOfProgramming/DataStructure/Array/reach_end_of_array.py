def can_reach_end(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > 0:
        for i in reversed(range(arr[0])):
            if can_reach_end(arr[i + 1 :]):
                return True
    return False


print(can_reach_end([3, 3, 0, 0, 2, 0, 1]))
print(can_reach_end([0, 3]))
print(can_reach_end([1, 0]))
print(can_reach_end([1, 0, 1]))
print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
