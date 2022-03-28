class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, node):
        return self.root[node]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.find(i) == rootY:
                    self.root[self.find(i)] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 2))
print(uf.connected(1, 5))
print(uf.connected(1, 8))
