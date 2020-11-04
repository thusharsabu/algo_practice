# Implement a linked list class. Your class should be able to:

#   Append data to the tail of the list and prepend to the head
#   Search the linked list for a value and return the node
#   Remove a node
#   Pop, which means to return the first node's value and delete the node from the list
#   Insert data at some position in the list
#   Return the size (length) of the linked list
# import pdb; pdb.set_trace()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def append(self, value):
        current_node = self.head
        new_node = Node(value)

        if current_node is None:
            self.head = new_node
            return

        while current_node is not None and current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def search(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        return current_node

    def remove(self, value):
        current_node = self.head

        if current_node is None:
            return

        if current_node.value is value:
            self.head = current_node.next

        while current_node and current_node.next:
            if current_node.next.value == value:
                temp = current_node.next
                current_node.next = current_node.next.next

            current_node = current_node.next

        return None

    def pop(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next

        return temp

    def insert_at_pos(self, value, pos):
        current_node = self.head

        for _ in range(1, pos - 1):
            current_node = current_node.next

        temp = current_node.next
        current_node.next = Node(value)
        current_node.next.next = temp

    def size(self):
        current_node = self.head
        size = 0

        while current_node:
            size += 1
            current_node = current_node.next

        return size

    def to_list(self):
        arr = []
        current_node = self.head
        while current_node:
            arr.append(current_node.value)
            current_node = current_node.next

        return arr


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [
    5,
    2,
    1,
    4,
    3,
], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"