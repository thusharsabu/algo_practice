# Reverse a singly linked list
from linked_list import LinkedList

def reverse(linked_list):
    new_head = None
    current_node = linked_list.head
    while current_node:
        next_pointer = current_node.next
        current_node.next = new_head
        new_head = current_node
        current_node = next_pointer
    linked_list.head = new_head


# Reverse Linked List from nth node to mth node

def reverse_sublist(n_pos, m_pos):
  


linked_list = LinkedList()
linked_list.add_from_array(list(range(10)))
linked_list.print_list()
reverse(linked_list)
print("Reverse Linked list: ")
linked_list.print_list()
