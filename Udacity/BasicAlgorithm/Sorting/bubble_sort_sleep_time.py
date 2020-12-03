# Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep,
# sort the times from latest to earliest.

# def bubble_sort_2(l):
#     # TODO: Implement bubble sort solution
#     pass

# bubble_sort_2(sleep_times)
# print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")

def bubble_sort_2(l):
  len_l = len(l)

  for f_index in range(len_l):
    for index in range(1, len_l - f_index):
      if l[index][0] == l[index - 1][0]:
        if l[index][1] > l[index - 1][1]:
          temp = l[index]
          l[index] = l[index - 1]
          l[index - 1] = temp
      elif l[index][0] > l[index - 1][0]:
          temp = l[index]
          l[index] = l[index - 1]
          l[index - 1] = temp
  return l

sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")


