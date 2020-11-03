# Implement an algorithm to find the kth to last element of a singly linked list.

from linked_list import LinkedList

def find_kth_element(linked_list, element):
  current_node = linked_list.head
  length = 0
  while current_node:
    length += 1
    current_node = current_node.next
  length -= element + 1
  count = 0
  current_node = linked_list.head
  while count <= length:
    current_node = current


