
def search(arr, target):

    def binary_search(left, right):
      if left > right: return -1

      mid = (left + right) // 2
      # print("start {}, End {}".format(left, right))
      if arr[mid] == target:
        return mid
      
      if arr[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
      return binary_search(left, right)

    return binary_search(0, len(arr) - 1)


print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0))
print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1))


