"""Tree is an example of non-linear data structures. A tree structure is a way of representing the hierarchical nature of a structure in a graphical form"""

class TreeNode:
  def __init__(self, name=None, destination=None, parent=None):
    self.name = name 
    self.destination = destination
    self.parent = parent 
    self.children = []
    
  def __repr__(self):
    return f'Node({self.name})'
    
  def print_tree(self, typ):
    if typ == "name":
      self.name_tree(typ)
    elif typ == "destination":
      self.destination_tree(typ)
    elif typ == "both":
      space = " " * self.get_level() * 3
      prefix = space + "|--" if self.parent else ""
      
      print(prefix + self.name + f" ({self.destination})")
      if self.children:
        for child in self.children:
          child.print_tree(typ)
    
  def name_tree(self, typ):
    space = " " * self.get_level() * 3
    prefix = space + "|--" if self.parent else ""
    
    print(prefix + self.name)
    if self.children:
      for child in self.children:
        child.print_tree(typ)
    
  def destination_tree(self, typ):
    space = " " * self.get_level() * 3
    prefix = space + "|--" if self.parent else ""
    
    print(prefix + self.destination)
    if self.children:
      for child in self.children:
        child.print_tree(typ)
    
  def add_child(self, name, destination=None):
    self.children.append(TreeNode(name, destination=destination, parent=self))
    
  def add_childNode(self, node):
    self.children.append(node)
    
  def get_level(self):
    level = 0
    parent = self.parent
    if parent == None:
      return level
    while parent:
      level = level + 1
      parent = parent.parent
    return level 
    
  def delete_child(self, name):
    parent = self.parent
    for child in parent.children:
      if child == name:
        parent.children.remove(name)
      parent = child.parent
        
  def search(self, data):
    children = []
    if self.children:
      for child in self.children:
        children.append(child)
        
    while children:
      for child in children:
        if child.name == data:
          return child.parent.name
        children.remove(child)
        children += child.children
        
  def size(self):
    size = 1 
    if self.children:
      size += len(self.children)
    return size 
    
  def depth(self):
    yield self 
    for child in self.children:
      yield from child.depth()



if __name__=="__main__":
  elect = TreeNode("Electronics")
  phones = TreeNode("Phones", parent=elect)
  tv = TreeNode("Tv", parent=elect)
  laptop = TreeNode("Laptops", parent=elect)
  
  elect.add_childNode(phones)
  elect.add_childNode(tv)
  elect.add_childNode(laptop)
  
  phones.add_child("iPhones")
  phones.add_child("Techno")
  phones.add_child("Samsung")
  
  tv.add_child("Samsung")
  tv.add_child("LG")
  tv.add_child("Hisense")
  
  hp = TreeNode("Hp", parent=laptop)
  dell = TreeNode("Dell", parent=laptop)
  soft = TreeNode("Microsoft", parent=laptop)
  laptop.add_childNode(dell)
  laptop.add_childNode(hp)
  laptop.add_childNode(soft)
  
  hp.add_child("01")
  
  elect.print_tree("name")
  print(tv.get_level())
  print(tv.size())
  print(hp.size())
  print(elect.size())
  print(elect.search("Samsung"))
  ceo = TreeNode("Nilupul", "CEO")
  cto = TreeNode("Chinmay", "CTO", parent= ceo)
  hr = TreeNode("Gel", "HR Head", parent=ceo)
  
  hr.add_child("Peter", "Recruitment Manager")
  hr.add_child("Waqas", "Policy Manager")
  
  ih = TreeNode("Vishaw", "Infrastructure Head", parent=cto)
  ih.add_child("Dhaval", "Cloud Manager")
  ih.add_child("Abhijit", "App Manager")
  
  ah = TreeNode("Aamir", "Application Head", parent=cto)
  
  cto.add_childNode(ih)
  cto.add_childNode(ah)
  
  ceo.add_childNode(cto)
  ceo.add_childNode(hr)
  print()
  ceo.print_tree("both")
  
  for c in ceo.depth():
    print(c)