# Problem-3:
#
# Give an algorithm to insert an elemnt into binary tree

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


def insert(root, node):
    if root is None or node is None:
        return

    queue = [root]

    while queue:
        c_node = queue.pop(0)

        if not c_node.has_right_child():
            c_node.set_right_child(node)
            return
        else:
            queue.append(c_node.get_right_child())

        if not c_node.has_left_child():
            c_node.set_left_child(node)
            return
        else:
            queue.append(c_node.get_left_child())


def pre_order_recursive(root, result):

    if root is None:
        return

    result.append(root.value)
    pre_order_recursive(root.left, result)
    pre_order_recursive(root.right, result)

    return result


print("Recursive: ")
print(pre_order_recursive(tree.get_root(), []))

insert(tree.get_root(), Node(143))

print("Recursive: ")
print(pre_order_recursive(tree.get_root(), []))
