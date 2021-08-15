from heapq import heappop, heappush


def dijkstras(start, goal, graph):
    visited = set()
    shortest_distance = {}
    pred = {}

    for node in graph:
        shortest_distance[node] = float("inf")
    print(f"The shor {shortest_distance}")
    shortest_distance[start] = 0

    q = [(0, start)]

    while q:
        dist, node = heappop(q)
        if node in visited:
            continue

        for child, child_dist in graph[node].items():
            if child in visited:
                continue
            if dist + child_dist < shortest_distance[child]:
                shortest_distance[child] = dist + child_dist
                heappush(q, (dist + child_dist, child))
                pred[child] = node
    print(pred)
    return shortest_distance


graph = {
    "a": {"b": 10, "c": 3},
    "b": {"c": 1, "d": 2},
    "c": {"b": 4, "d": 8, "e": 2},
    "d": {"e": 7},
    "e": {"d": 9},
}
# graph = {'a': {'b': 3, 'c': 4}}
print(dijkstras("a", "d", graph))
