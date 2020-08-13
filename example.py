from shortpath import Graph

data = [('A','B',3),('A','C',2),('A','D',9),('B','E',3),('C','D',5),('D','E',2),('E','F',1)]

# Create new graph with graph.txt
newGraph = Graph(data='graph.txt') 

# or you can use data list.
# newGraph = Graph(data=data) 

# toEverywhere. With this method, you find the shortest path between the starting node and all other nodes.
print(newGraph.toEverywhere('A'))

# toANode, With this method, you find the shortest path between the start node and the end node.
print(newGraph.toANode('A', 'F'))

# nearestNode. With this method, you find the node closest to the node you chose.
print(newGraph.nearestNode('A'))

# With this method, you find the node furthest from the node you chose
print(newGraph.furthestNode('A'))

# OUTPUT:
# {'A': 0, 'B': 3.0, 'C': 2.0, 'D': 7.0, 'E': 6.0, 'F': 7.0}
# 7.0
# C
# D
