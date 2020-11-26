# Find the Value in a Binary Tree

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
#     /   \
#   1     81


def max_value(root, max_data):
    if root is None:
        return max_data

    if root.value > max_data:
        max_data = root.value

    max_data = max_value(root.get_left_child(), max_data)
    max_data = max_value(root.get_right_child(), max_data)

    return max_data


print("Recursive: ")
print(max_value(tree.get_root(), float("-infinity")))


def max_value_iterative(root, max_data):
    if root is None:
        return max_data

    stack = [root]

    while stack:
        node = stack.pop()
        if node.value > max_data:
            max_data = node.value

        if node.has_right_child():
            stack.append(node.get_right_child())

        if node.has_left_child():
            stack.append(node.get_left_child())

    return max_data


print("Iterative: ")
print(max_value_iterative(tree.get_root(), float("-infinity")))
