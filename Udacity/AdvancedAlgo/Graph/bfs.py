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

    def bfs_search(self, node, value, visited):
        if node is None:
            return None

        queue = [node]

        while len(queue) > 0:
            current_node = queue.pop(0)

            visited.append(current_node)
            if current_node.value == value:
                return current_node

            for child in current_node.children:
                if child not in visited:
                    queue.append(child)


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

# print(graph1.bfs_search(nodeG, "S").value)
print(graph1.bfs_search(nodeG, "S", []).value)
