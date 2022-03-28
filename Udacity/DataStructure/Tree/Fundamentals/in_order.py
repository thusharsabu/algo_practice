from tree import Tree
from tree import Node
from stack import Stack

# Create Tree with data

tree = Tree(Node("apple"))
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
tree.get_root().get_left_child().set_right_child(Node("Mango"))

#         apple
#         /   \
#     banana   cherry
#     /   \
# dates  Mango


def in_order_recursive(root, result):
    if root is None:
        return

    if root.has_left_child():
        in_order_recursive(root.get_left_child(), result)
    result.append(root.value)
    if root.has_right_child():
        in_order_recursive(root.get_right_child(), result)

    return result


print("Recursive: ")
print(in_order_recursive(tree.get_root(), []))


def in_order_iterative(root, result):
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.get_left_child()

        else:
            value = stack.pop()
            result.append(value.value)
            node = value.get_right_child()
    return result


def in_order_iterative1(root, result):
    if root is None:
        return

    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.get_left_child()
        else:
            node = stack.pop()
            result.append(node.value)
            node = node.get_right_child()

    return result


print("Iterative: ")
print(in_order_iterative(tree.get_root(), []))
