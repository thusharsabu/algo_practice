class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.did_visit = False

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)


class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

    def dfs_search(self, root_node, value):
        if root_node not in self.nodes:
            return None
        stack = [root_node]
        visited = []
        
        while len(stack) > 0:
            current_node = stack.pop()
            visited.append(current_node)

            if current_node.value == value:
                return current_node
            else:
                for child in current_node.children:
                    if child not in visited:
                        stack.append(child)

    def dfs_search_recursion(self, root_node, value, visited):
      if root_node is None:
        return None
      print("The current_nodeis: {}".format(root_node.value))
      if root_node.value == value:
        return root_node

      visited.append(root_node)

      for child in root_node.children:
        if child not in visited:
          a = self.dfs_search_recursion(child, value, visited)

          if a is not None:
            return a


nodeG = GraphNode("G")
nodeR = GraphNode("R")
nodeA = GraphNode("A")
nodeP = GraphNode("P")
nodeH = GraphNode("H")
nodeS = GraphNode("S")

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

print(graph1.dfs_search(nodeG, "S").value)
print(graph1.dfs_search_recursion(nodeG, "S", []).value)
