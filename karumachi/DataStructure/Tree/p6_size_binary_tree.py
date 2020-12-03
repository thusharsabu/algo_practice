# Problem 6
#
# Find the size of binary tree


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


def size(root):
    if root is None:
        return 0

    return size(root.get_left_child()) + size(root.get_right_child()) + 1


print("Recursive: ")
print(size(tree.get_root()))


def size_iterative(root):
    if root is None:
        return 0

    stack = [root]
    count = 0

    while stack:
        node = stack.pop()
        count += 1

        if node.has_right_child():
            stack.append(node.get_right_child())

        if node.has_left_child():
            stack.append(node.get_left_child())

    return count


print("Iterative: ")
print(size_iterative(tree.get_root()))
