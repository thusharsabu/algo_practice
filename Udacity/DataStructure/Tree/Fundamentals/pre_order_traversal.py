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

# Depth first, pre-order traversal with a stack¶
# pre-order traversal of the tree would visit the nodes in this order:

# apple, banana, dates, cherry

# Recursive:
# def pre_order(root, result):
#     if root is None:
#         return

#     result.append(root.value)
#     pre_order(root.get_left_child(), result)
#     pre_order(root.get_right_child(), result)

#     return result


# print("Recursive: ")
# print(pre_order(tree.get_root(), []))


# def pre_order_iterative(root, result):
#     stack = Stack()
#     stack.push(root)

#     while not stack.is_empty():
#         current_node = stack.pop()
#         result.append(current_node.value)
#         if current_node.has_right_child():
#             stack.push(current_node.get_right_child())
#         if current_node.has_left_child():
#             stack.push(current_node.get_left_child())

#     return result

# print("Iterative: ")
# print(pre_order_iterative(tree.get_root(), []))


def pre_order_recursive(root, result):

    if root is None:
        return

    result.append(root.value)
    pre_order_recursive(root.left, result)
    pre_order_recursive(root.right, result)

    return result


print("Recursive: ")
print(pre_order_recursive(tree.get_root(), []))


def pre_order_iterative1(root, result):
    if root is None:
        return result

    stack = []
    node = root
    visited = set()

    while stack or node:
        if node:
            result.append(node.value)
            stack.append(node)
            node = node.get_left_child()
        else:
            node = stack.pop()

            if node not in visited and node.has_right_child():
                visited.add(node)
                node = node.get_right_child()
            else:
                node = None
    return result


def pre_order_iterative1(root, result):
    if root is None:
        return
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.has_right_child():
            stack.append(node.get_right_child())
        if node.has_right_child():
            stack.append(node.get_left_child())

    print("Result from here: ")
    return result


def pre_order_iterative(root, result):
    if root is None:
        return

    node = root
    stack = []

    while node or stack:
        if node:
            result.append(node.value)
            stack.append(node)
            node = node.get_left_child()
        else:
            node = stack.pop()
            node = node.get_right_child()
    return result


print("Iterative: ")
print(pre_order_iterative(tree.get_root(), []))
