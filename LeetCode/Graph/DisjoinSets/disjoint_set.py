class DisjointClass:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, node):
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:

            for i in range(len(self.root)):
                if self.root[i] == root2:
                    self.root[i] = root1

    def connected(self, node1, node2):
        return self.root[node1] == self.root[node2]


uf = DisjointClass(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 2))
print(uf.connected(1, 5))
print(uf.connected(1, 8))
# print(uf.conneceted())
# print(uf.conneceted())
