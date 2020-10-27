# Remove Dups
# Write code to remove duplicates from an unsorted linked list.
# Follow-up question
# How would solve this problem if a temporary buffer is not allowed.
from linked_list import LinkedList

def remove_duplicates_with_memory(linked_list):
  clean_value = {}
  current_node = linked_list.head
  prev = current_node
  while current_node:
    if current_node.value in clean_value:
      if current_node.next is None:
        prev.next = None
        current_node = None
      else:
        prev.next = current_node.next
        current_node = current_node.next
    else:
      clean_value[current_node.value] = None
      prev = current_node
      current_node = current_node.next

def remove_without_memory(linked_list):
  current_node = linked_list.head
  while current_node:
    prev = current_node
    current_value = current_node.value
    next_value = current_node.next
    while next_value:
      if next_value.value is current_value:
        prev.next = next_value.next
        next_value = next_value.next
      else:
        prev = next_value
        next_value = next_value.next
    current_node = current_node.next

linked_list = LinkedList()
linked_list.create_list([1,2,3,4,1,2,3,4,5,6,7,7])
linked_list.print_linked_list()
remove_duplicates_with_memory(linked_list)
print("")
print("Remove Duplicates")
linked_list.print_linked_list()
linked_list.create_list([1,1,1,1,2,2,2,3,3,4,1,2,3,4,5,6,7,7])
linked_list.print_linked_list()
remove_duplicates_with_memory(linked_list)
print("")
print("Remove Duplicates")
linked_list.print_linked_list()

# --------------------------------------
print("")
print("Without memory: ")
linked_list = LinkedList()
linked_list.create_list([1,1,1,1,2,2,2,3,3,4,1,2,3,4,5,6,7,7])
linked_list.print_linked_list()
remove_without_memory(linked_list)
print("")
print("Remove Duplicates")
linked_list.print_linked_list()
