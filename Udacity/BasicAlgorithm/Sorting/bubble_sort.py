# Bubble sort


# def bubble_sort(arr):
#     changed_true = True
#     i = j = 0
#     len_arr = len(arr)
#     while changed_true:
#         i += 1
#         len_arr -= 1
#         changed_true = False
#         for index in range(len_arr):
#             j += 1
#             if (index + 1) < len(arr):
#                 if arr[index] > arr[index + 1]:
#                     temp = arr[index]
#                     arr[index] = arr[index + 1]
#                     arr[index + 1] = temp
#                     changed_true = True
#     print("i " + str(i))
#     print("j " + str(j))
#     return arr

def bubble_sort(arr):
    sorted = False
    count = 0
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            count += 1
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(count)
    return arr


print(bubble_sort([7, 6, 5, 4, 3, 2, 1]))
print(bubble_sort([234, 123, 55, 242, 7, 32, 1, 123, 5, 0]))
