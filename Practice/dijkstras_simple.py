import math
from heapq import heappush,heappop

def dijkstra(start, goal):
    shortest_distance = {}
    # unseenNodes = graph
    predecessor = {}
    path = []
    visited = set()

    q = [(0,start)]

    for node in graph:
        shortest_distance[node] = math.inf
    shortest_distance[start] = 0
    while q:
        dist, node = heappop(q)
        if node not in visited:
            visited.add(node)
            for child, child_dist in graph[node].items():
                print(f"sd mins #{shortest_distance}")

                if child in visited:
                    continue

                if child_dist + dist < shortest_distance[child]:
                    shortest_distance[child] = child_dist + dist
                    predecessor[child] = node
                    heappush(q,(child_dist + dist, child))
            print(f"queue #{q}")
            print(f"visited #{visited}")
            print(f"predec #{predecessor}")

# graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
graph = {'a': {'b': 3, 'c': 4}}
print(dijkstra('a','d'))