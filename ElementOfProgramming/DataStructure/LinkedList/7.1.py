# Merge two sorted linked list
from linked_list import LinkedList
from linked_list import Node

def merge_sorted_list(l1, l2):
  dummy_head = node = Node(None)

  while l1 and l2:
    if l1.value < l2.value:
      node.next, l1 = l1, l1.next
    else:
      node.next, l2 = l2, l2.next
  
  node.next = l1 or l2
  return dummy_head.next


linked_list1 = LinkedList()
linked_list1.add_from_array(list(range(10)))

linked_list2 = LinkedList()
linked_list1.add_from_array(list(range(20, 30)))

a = merge_sorted_list(linked_list2.head, linked_list1.head)

new_l = LinkedList()
new_l.head = a
new_l.print_list()


