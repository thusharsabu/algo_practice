# Problem-3
#
# Give an Algorithm for searching an element in binary tree.


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


def search(root, value):
    if root is None or value is None:
        return False

    if root.value is value:
        return root
    else:
        found = search(root.get_left_child(), value)

        if found:
            return found
        else:
            return search(root.get_right_child(), value)


print("Recursive: ")
print(search(tree.get_root(), 900))


def search_iterative_dfs(root, value):
    if root is None or value is None:
        return None

    stack = [root]

    while stack:
        node = stack.pop()
        if node.value == value:
            return node
        if node.has_right_child():
            stack.append(node.get_right_child())

        if node.has_left_child():
            stack.append(node.get_left_child())

    return False


print("Iterative DFS: ")
print(search_iterative_dfs(tree.get_root(), 43))


def search_iterative_bfs(root, value):
    if root is None or value is None:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)

        if node.value == value:
            return node

        if node.has_left_child():
            queue.append(node.get_left_child())
        if node.has_right_child():
            queue.append(node.get_right_child())

    return False


print("Iterative BFS: ")
print(search_iterative_bfs(tree.get_root(), 600))