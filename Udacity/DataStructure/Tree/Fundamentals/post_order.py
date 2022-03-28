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

# Post Order: Visit all left subtree, visit all right sub-tree then current node
# Expected post_order output:
# ['dates', 'Mango', 'banana', 'cherry', 'apple']


def post_order_recursive(root, result):
    if root is None:
        return

    post_order_recursive(root.get_left_child(), result)
    post_order_recursive(root.get_right_child(), result)
    result.append(root.value)

    return result


print("Recursive: ")
print(post_order_recursive(tree.get_root(), []))


def post_order_iterative(root, result):
    stack = []
    visited = set()
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.get_left_child()
        else:
            node = stack.pop()

            if node in visited or node.get_right_child() is None:
                result.append(node.value)
                node = None
            else:
                visited.add(node)
                stack.append(node)
                node = node.get_right_child()
    return result


def post_order_iterative1(root, result):
    if root is None:
        return None

    stack = []
    visited = set()
    node = root

    while node or stack:
        if node:
            stack.append(node)
            node = node.get_left_child()
        else:
            node = stack.pop()

            if node.get_right_child() and not node in visited:
                stack.append(node)
                visited.add(node)
                node = node.get_right_child()
            else:
                result.append(node.value)
                node = None

    return result


print("Iterative: ")
print(post_order_iterative(tree.get_root(), []))
