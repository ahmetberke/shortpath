from dijkstra import Graph

# Create new graph with graph.txt
newGraph = Graph(filename="graph.txt")

# toEverywhere. With this method, you find the shortest path between the starting node and all other nodes.
print(newGraph.toEverywhere('A'))

# toANode, With this method, you find the shortest path between the start node and the end node.
print(newGraph.toANode('A', 'F'))


# OUTPUT:
# {'A': 0, 'B': 3.0, 'C': 2.0, 'D': 7.0, 'E': 6.0, 'F': 7.0}
# 7.0