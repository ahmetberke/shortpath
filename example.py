from dijkstra import Graph

# Create new graph with graph.txt
newGraph = Graph(filename="graph.txt")
print(newGraph.dijkstra_algorithm('A'))
