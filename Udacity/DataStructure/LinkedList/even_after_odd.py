# Problem Statement
# Given a linked list with integer data, arrange the elements in such a manner that all nodes
# with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any
# other data structure. The relative order of even and odd elements must not change.

# Example:

# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, arr):
        if self.head == None:
            current_node = Node(arr[0])
            self.head = current_node
        else:
            current_node = self.get_tail()
            current_node.next = Node(arr[0])
            current_node = current_node.next

        for element in arr[1:]:
            current_node.next = Node(element)
            current_node = current_node.next

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(str(current_node.value) + " ->", end="")
            current_node = current_node.next
        print("")

    def get_tail(self):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        return current_node


def even_after_odd1(head, linked_list):
    tail = find_tail(head)
    current_node = head
    prev = head
    first_occurence = None
    while current_node is not None:
        if first_occurence == current_node:
            return head
        # linked_list.print_linked_list()
        if current_node.value % 2 == 0:
            if current_node.next is not None:
                if current_node == head:
                    print("not reaching here: ")
                    head = current_node.next
                    current_node.next = None
                    tail.next = current_node
                    tail = tail.next
                    current_node = head
                    prev = head
                else:

                    prev.next = current_node.next
                    current_node.next = None
                    linked_list.print_linked_list()
                    tail.next = current_node
                    tail = tail.next
                    current_node = prev.next
                    print("After exchange")
                    linked_list.print_linked_list()
            else:
                prev = current_node
                current_node = current_node.next
            if first_occurence == None:
                first_occurence = tail
        else:
            prev = current_node
            current_node = current_node.next
    return head


head = Node


def find_tail(head):
    while head.next is not None:
        head = head.next
    return head


class EvenAfterOdd:
    def __init__(self) -> None:
        self.even = None
        self.odd = None
        self.evenTail = None
        self.oddTail = None

    def addEven(self, node):
        if self.even:
            self.evenTail.next = node
            self.evenTail = node
        else:
            self.even = node
            self.evenTail = node

        self.evenTail.next = None

    def addOdd(self, node):
        if self.odd:
            self.oddTail.next = node
            self.oddTail = node
        else:
            self.odd = node
            self.oddTail = node

        self.oddTail.next = None

    def combine(self, ll):
        self.oddTail.next = self.even

        ll.head = self.odd

    def evenAfterOdd(self, ll):
        current = ll.head

        while current:
            value = current
            current = current.next

            if value.value % 2 == 0:
                self.addEven(value)
            else:
                self.addOdd(value)
        self.combine


linked_list = LinkedList()
linked_list.create_list([1, 2, 3, 4, 5, 6])
# linked_list.print_linked_list()

eo = EvenAfterOdd()
eo.evenAfterOdd(linked_list)
eo.combine(linked_list)
print("")
# even_after_odd(linked_list.head, linked_list)
print("Output")
linked_list.print_linked_list()
