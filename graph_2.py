from single_linked_list import SingleLinkedList

class Vertice:
  def __init__(self, data):
    self.data = data 
    self.connections = {}
    
  def addNeighbor(self, data, weight=0):
    self.connections[data] = weight
    
class Graph:
  def __init__(self):
    self.dictionary = {}
    self.count = 0
    
  def __iter__(self): 
    return iter(self.dictionary.values())
    
  def add_vert(self, data):
    vert = Vertice(data)
    self.dictionary[data] = vert 
   
  def add_edge(self, fro, to, weight=0):
    if fro not in self.dictionary:
      self.add_vert(fro)
    if to not in self.dictionary:
      self.add_vert(to)
      
    node = self.dictionary[fro]
    node.addNeighbor(self.dictionary[to], weight)
    
  def get_vert(self, data):
    if data in self.dictionary:
      return self.dictionary[data].data
    return None 
    
  def get_vertices(self):
    return self.dictionary.keys()
    
  def get_edges(self):
    edges = []
    for v in self:
      for w, c in v.connections.items():
        vid = v.data
        wid = w.data
        edges.append((vid, wid, c))
    return edges

  def get_path(self, start, end, path=[]):
    if start and end in self.dictionary:
      startVert = self.dictionary[start]
      endVert = self.dictionary[end]
    else:
      return None
    path = path + [startVert.data]
    
    if start == end:
      return [path]
      
    paths = []
    for node in startVert.connections:
      if node not in path:
        new_path = self.get_path(node.data, end, path)
        for p in new_path:
          paths.append(p)
    return paths

  def get_shortest_path(self, start, end, path=[]):
    if start and end in self.dictionary:
      startVert = self.dictionary[start]
      endVert = self.dictionary[end]
    else:
      return None
    path = path + [startVert.data]
    
    if start == end:
      return [path]
      
    shortest_path = None
    for node in startVert.connections:
      if node not in path:
        sp = self.get_shortest_path(node.data, end, path)
        if sp:
          if shortest_path == None or len(sp) < len(shortest_path):
            shortest_path = sp
    return shortest_path


  def shortest_path_weight(self, start, end, path=[]):
    weightsum = None 
    final = None
    paths = self.get_path(start, end)
    for path in paths:
      l = SingleLinkedList()
      for data in path:
        l.push(self.dictionary[data])
      weight = 0
      head = l.head
      while head.next:
        nxt_data = head.next.value.data
        weight += head.value.connections[self.dictionary[nxt_data]]
        head = head.next
      if weightsum == None or weight < weightsum:
          weightsum = weight 
          final = path 
      print(weightsum)
    return final


if __name__=="__main__":
  routes = [
    ("Nigeria", "Dubai"),
    ("Nigeria", "Paris"),
    ("Paris", "New York"),
    ("Paris", "Dubai"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
    ]
    
  G = Graph()
  G.add_edge("Nigeria", "Dubai", 4)
  G.add_edge("Nigeria", "Paris", 2)
  G.add_edge("Paris", "New York", 6)
  G.add_edge("Paris", "Dubai", 1)
  G.add_edge("Dubai", "New York", 4)
  G.add_edge("New York", "Toronto", 2)
  print(G.get_vert("Nigeria"))
  print(G.get_vertices())
  print(G.get_edges())
  print(G.get_path("Nigeria", "Toronto"))
  print(G.get_shortest_path("Nigeria", "Toronto"))
  print(G.shortest_path_weight("Nigeria", "Toronto"))
  #print(G.get_longest_path("Nigeria", "Toronto"))
  