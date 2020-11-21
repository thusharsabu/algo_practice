from tree import Tree
from tree import Node
from stack import Stack

# Create Tree with data

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# Depth first, pre-order traversal with a stack¶
# pre-order traversal of the tree would visit the nodes in this order:

# apple, banana, dates, cherry
