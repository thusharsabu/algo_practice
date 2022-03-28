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


def level_order(root, result):
    print("new One")
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.value)

            queue.append(node.get_right_child())
            queue.append(node.get_left_child())
    return result


def level_order(root, result):
    if result is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        if node is not None:
            result.append(node.value)

            if node.has_left_child():
                queue.append(node.get_left_child())

            if node.has_right_child():
                queue.append(node.get_right_child())
    return result


print("Iterative: ")
print(level_order(tree.get_root(), []))
