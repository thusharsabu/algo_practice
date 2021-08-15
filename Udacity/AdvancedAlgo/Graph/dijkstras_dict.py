graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}

def dijkstras(graph, start, goal):
  unvisited = graph
  shortest_distance = {}
  predecessor = {}

  for node in unvisited:
    shortest_distance[node] = float('inf')
  shortest_distance[start] = 0

  while unvisited:
    minNode = None

    for node in unvisited:
      if minNode is None:
        minNode = node
      elif shortest_distance[node] < shortest_distance[minNode]:
        minNode = node

    for node, weight in graph[minNode].items():
      current_weight = shortest_distance[minNode] + weight

      if current_weight < shortest_distance[node]:
        shortest_distance[node] = current_weight
        predecessor[node] = minNode
    
    unvisited.pop(minNode)

  return [shortest_distance, predecessor]

a = dijkstras(graph, 'a', 'e')
print("Shortest distance: {}".format(a[0]))
print("Predecessor: {}".format(a[1]))

