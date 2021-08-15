from heapq import heappush, heappop
import collections


def networdDelayTimes(times, n, k):
    graph = collections.defaultdict(list)
    dist = {}
    seen = set([])

    for u, v, w in times:
        graph[u].append((v, w))
        if u not in dist:
            dist[u] = float("inf")
        if v not in dist:
            dist[v] = float("inf")
    dist[k] = 0

    q = [(0, k)]
    while q:
      dist_, node = heappop(q)
      seen.add(node)
      for child, child_dist in graph[node]:
        if child not in seen:
          if child_dist + dist_ < dist[child]:
            dist[child] = child_dist + dist_
          heappush(q, (dist[child], child))
    
    current_max = max(dist.values())
    if len(seen) == n and current_max is not float('inf'): return current_max

    return -1




print(networdDelayTimes([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(networdDelayTimes([[1,2,1]], 2, 1))
print(networdDelayTimes([[1,2,1]], 2, 2))
print(networdDelayTimes([[1,2,1],[2,1,3]], 2, 2))

