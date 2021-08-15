# Problem Statements
# In an ocean, there are n islands some of which are connected via bridges. Travelling over a bridge has some cost attaced with it. Find bridges in such a way that all islands are connected with minimum cost of travelling.

# You can assume that there is at least one possible way in which all islands are connected with each other.

# You will be provided with two input parameters:

# num_islands = number of islands

# bridge_config = list of lists. Each inner list will have 3 elements:

#  a. island A
#  b. island B
#  c. cost of bridge connecting both islands
# Each island is represented using a number

# Example:

# num_islands = 4
# bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
# Input parameters explanation: 1. Number of islands = 4 2. Island 1 and 2 are connected via a bridge with cost = 1 Island 2 and 3 are connected via a bridge with cost = 4 Island 1 and 4 are connected via a bridge with cost = 3 Island 4 and 3 are connected via a bridge with cost = 2 Island 1 and 3 are connected via a bridge with cost = 10

# In this example if we are connecting bridges like this...

# between 1 and 2 with cost = 1
# between 1 and 4 with cost = 3
# between 4 and 3 with cost = 2
# ...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.

def connecting_islands(num_islands, connections):
  graph = {}
  for first, second, weight in connections:
    if first in graph:
      graph[first][second] = weight
    else:
      graph[first] = {}
      graph[first][second] = weight
    
    if second in graph:
      graph[second][first] = weight
    else:
      graph[second] = {}
      graph[second][first] = weight
      
  print(graph)



connecting_islands(4, [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]])
  


