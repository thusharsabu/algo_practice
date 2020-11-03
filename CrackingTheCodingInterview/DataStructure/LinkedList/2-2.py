# Implement an algorithm to find the kth to last element of a singly linked list.

from linked_list import LinkedList

# Get count and then parse until kth element from end.
def find_kth_element(linked_list, element):
    current_node = linked_list.head
    length = 0
    while current_node:
        length += 1
        current_node = current_node.next
    length -= element + 1
    count = 0
    current_node = linked_list.head
    while current_node and count <= length:
        current_node = current_node.next
        count += 1
    if current_node == None:
      return None
    else:
      return current_node.value


def find_kth_element_(linked_list, kth_element):
    current_node = linked_list.head
    count = 1
    k_element = current_node

    while current_node:
        if count >= kth_element + 1:
            k_element = k_element.next

        current_node = current_node.next
        count += 1
    return k_element.value


linked_list = LinkedList()
linked_list.create_list(list(range(1, 11)))
print(find_kth_element_(linked_list, 10))
print(find_kth_element(linked_list, 10))
