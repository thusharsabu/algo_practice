class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        current_node = self.head
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            current_node = self.get_tail(current_node)
            current_node.next = new_node

    def add_from_array(self, arr):
        new_node = Node(arr[0])
        if self.head is None:
            self.head = new_node
            current_node = new_node
        else:
            current_node = self.get_tail(self.head)
            current_node.next = new_node
            current_node = new_node

        for element in arr[1:]:
            current_node.next = Node(element)
            current_node = current_node.next

    def delete_by_value(self, value):
        current_node = self.head

        prev_node = None
        while current_node:
            if current_node.value is value:
                if prev_node is None:
                    self.head = current_node.next
                    current_node = current_node.next
                else:
                    prev_node.next = current_node.next
                    current_node = current_node.next
            else:
                prev_node = current_node
                current_node = current_node.next
        return current_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def get_tail(self, node):
        current_node = node
        while current_node.next:
            current_node = current_node.next

        return current_node

