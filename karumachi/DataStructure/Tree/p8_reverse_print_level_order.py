# Problem 8
#
# Print level order in reverse order

from tree import Tree
from tree import Node

tree = Tree(Node(0))
tree.get_root().set_left_child(Node(5))
tree.get_root().set_right_child(Node(600))
tree.get_root().get_right_child().set_right_child(Node(900))
tree.get_root().get_left_child().set_left_child(Node(1))
tree.get_root().get_left_child().set_right_child(Node(81))

#           0
#         /   \
#       5     600
#     /   \     \
#   1     81     900


def reverse_level_order(root):
    if root is None:
        return None

    queue = [root]
    stack = []

    while queue:
        node = queue.pop(0)
        stack.append(node.value)

        if node.has_right_child():
            queue.append(node.get_right_child())

        if node.has_left_child():
            queue.append(node.get_left_child())
    print(stack)
    while stack:
        print(stack.pop())


reverse_level_order(tree.get_root())
