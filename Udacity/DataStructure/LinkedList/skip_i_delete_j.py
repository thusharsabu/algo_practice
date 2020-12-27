# Problem Statement
# You are given the head of a linked list and two integers, i and j. You have to retain the first i
# nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

# Example:

# linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
# i = 2
# j = 3
# Output = 1 2 6 7 11 12


from linked_list import LinkedList

def skip_i_delete_j(head, i, j):
  i_count = j_count = 0

  current_node = head
  prev = current_node
  while current_node is not None:
    if i_count < i:
      prev = current_node
      current_node = current_node.next
      i_count += 1
    elif j_count == j:
      i_count = 0
      j_count = 0
    else:
      prev.next = current_node.next
      current_node = prev.next
      j_count += 1
  return head


linked_list = LinkedList()
linked_list.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
skip_i_delete_j(linked_list.head, 2, 3)
linked_list.print_linked_list()
print()
linked_list = LinkedList()
linked_list.create_list([1, 2, 3, 4, 5])
skip_i_delete_j(linked_list.head, 2, 4)
linked_list.print_linked_list()
