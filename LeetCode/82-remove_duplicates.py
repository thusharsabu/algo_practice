# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the
# original list. Return the linked list sorted as well.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    new_head = ListNode()
    node = new_head
    prev = head

    current_node = head.next
    count = 1

    while current_node:
        print("The current node is {}".format(current_node.val))
        print_list(new_head)
        if current_node.val != prev.val:
            if count == 1:
                print("reached here")
                node.next = prev
                node = node.next

            count = 1
            prev = current_node
        else:
            count += 1
        current_node = current_node.next
    if count == 1:
      node.next = prev
    return new_head.next


def deleteDuplicates1(head):
    prev = ListNode(1)
    current = head
    count = 1
    current_node = head.next
    head = prev

    while current_node:
        if current_node.val != current.val:
            if count == 1:
                prev.next = current
                prev = prev.next
            current = current_node
            count = 1
        else:

            count += 1
        if current_node.next is None:
            break
        current_node = current_node.next
    if count == 1:
        prev.next = current
        prev.next.next = None
    else:
        prev.next = None

    return head.next


def print_list(head):
    current_node = head

    while current_node:
        print(current_node.val, end="")
        print(" => ", end="")
        current_node = current_node.next
    print(None)


head = ListNode(1)
temp_head = head
for value in [2, 3, 3, 4, 4, 5]:
    temp_head.next = ListNode(value)
    temp_head = temp_head.next


deleteDuplicates(head)
print_list(head)