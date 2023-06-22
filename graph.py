

class Graph:
    
  def __init__(self, edges):
    self.edges = edges 
    self.graph_dict = {} 
    
    for head, end in edges:
      if head in self.graph_dict:
        self.graph_dict[head].append(end)
      else:
        self.graph_dict[head] = [end]
        
      
  def get_path(self, start, end, path=[]):
    path = path + [start]
    
    if start == end:
      return [path]
    if start not in self.graph_dict:
      return "-->"
      
    paths = []
    for node in self.graph_dict[start]:
      if node not in path:
        new_path = self.get_path(node, end, path)
        for p in new_path:
          paths.append(p)
    return paths

  def shortest_path(self, start, end, path=[]):
    path = path + [start]
    if start == end:
      return path 
    if start not in self.graph_dict:
      return None 
    
    shortest_path = None
    for node in self.graph_dict[start]:
      if node not in path:
        sp = self.shortest_path(node, end, path)
        if sp:
          if shortest_path == None or len(sp) < len(shortest_path):
            shortest_path = sp
    return shortest_path
        
        
if __name__=="__main__":
  routes = [
    ("Nigeria", "Dubai"),
    ("Nigeria", "Paris"),
    ("Paris", "New York"),
    ("Paris", "Dubai"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
    ]
    
  G = Graph(routes)
  print(G.graph_dict)
  print()
  print(G.get_path("Nigeria", "Toronto"))
  print(G.shortest_path("Nigeria", "Toronto"))
  #print(G.get _path_2("Nigeria", "Toronto"))