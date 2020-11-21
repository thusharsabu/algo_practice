# Reversing a linked list exercise
# Given a singly linked list, return another linked list that is the reverse of the first.

from linked_list import LinkedList


def reverse(list):
    current_node = list.head
    prev = None

    while current_node:
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next

    list.head = prev


linked_list = LinkedList()
linked_list.create_list(list(range(1, 11)))
linked_list.print_linked_list()
reverse(linked_list)
print("After reverse: ")
linked_list.print_linked_list()
