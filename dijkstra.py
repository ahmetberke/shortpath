
class Graph:
  
  def __init__(self, filename):

    self.graph = {}
    self.nodes = []
    with open(filename) as fhandle:
      for line in fhandle:
        edge_from, edge_to, cost, *_ = line.strip().split(" ")
        try:
          self.graph[edge_from][edge_to] = float(cost)
        except KeyError:
          self.graph[edge_from] = {}
          self.graph[edge_from][edge_to] = float(cost)
        try:
          self.graph[edge_to][edge_from] = float(cost)
        except KeyError:
          self.graph[edge_to] = {}
          self.graph[edge_to][edge_from] = float(cost)
      
        if edge_from not in self.nodes:
          self.nodes.append(edge_from)

        if edge_to not in self.nodes:
          self.nodes.append(edge_to)
    
  def short_path(self, starting_node):

    # The list of nodes has been copied to the unvisited nodes variable
    unvisited_nodes = self.nodes.copy()

    # creating the nodes to visit variable
    nodes_to_visit = []

    # creating shortest way dic
    # and entering the list of nodes is assigned a value 0 to the starting node and infinite to the other nodes.
    shortest_way = {
      node : (0 if node == starting_node else float('inf')) for node in self.nodes
    } 

    # assigned a neighbor way value to neighbor nodes
    # and neighbor nodes adding to nodes to visit list 
    for node in self.graph[starting_node].keys():
      shortest_way[node] = self.graph[starting_node][node]
      nodes_to_visit.append(node)
    
    unvisited_nodes.remove(starting_node)

    while len(unvisited_nodes) != 0:
      # the current node becomes the zeroth item of the list of nodes to visit
      current_node = nodes_to_visit[0]

      # shortest way value of current variable assinged to distance variable
      distance = shortest_way[current_node]
      try:
      # enters neighbor nodes of the current node.
        for node in self.graph[current_node].keys():

          # Updates the shortest path dictionary if the sum of the distance of the current node and the distance - 
          # of the neighbor node to the current node is shorter than the shortest path of the node
          if (distance + self.graph[current_node][node] < shortest_way[node]):
            shortest_way[node] = distance + self.graph[current_node][node]
          
          # If the node is not on the to visit list and is in the unvisited nodes list, - 
          # the node is added to the to visit list
          if node not in nodes_to_visit and node in unvisited_nodes:
            nodes_to_visit.append(node)
      except KeyError:
        pass
      
      # current node remove from unvisited nodes and nodes to visit
      unvisited_nodes.remove(current_node)
      nodes_to_visit.remove(current_node)
    
    # Return shortest way dic
    return shortest_way

  def toEverywhere(self, starting_node):
    return self.short_path(starting_node)
  
  def toANode(self, starting_node, ending_node):
    short_path = self.short_path(starting_node)
    return short_path[ending_node]



            
        
    
    

