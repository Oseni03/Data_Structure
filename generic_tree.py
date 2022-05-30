"""Tree is an example of non-linear data structures. A tree structure is a way of representing the hierarchical nature of a structure in a graphical form"""

class TreeNode:
  def __init__(self, data=None, parent=None):
    self.data = data 
    self.parent = parent 
    self.children = []
    
  def print_tree(self):
    space = " " * self.get_level() * 3
    prefix = space + "|--" if self.parent else ""
    
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()
    
  def add_child(self, data):
    self.children.append(TreeNode(data, self))
    
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
    
  def delete_child(self, data):
    parent = self.parent
    for child in parent.children:
      if child == data:
        parent.children.remove(data)
      parent = child.parent
        
  def search(self, data):
    children = []
    if self.children:
      for child in self.children:
        children.append(child)
        
    while children:
      for child in children:
        if child.data == data:
          return child.parent.data
        children.remove(child)
        children += child.children
        
  def size(self):
    size = 1 
    if self.children:
      size += len(self.children)
    return size



if __name__=="__main__":
  elect = TreeNode("Electronics")
  phones = TreeNode("Phones", elect)
  tv = TreeNode("Tv", elect)
  laptop = TreeNode("Laptops", elect)
  
  elect.add_childNode(phones)
  elect.add_childNode(tv)
  elect.add_childNode(laptop)
  
  phones.add_child("iPhones")
  phones.add_child("Techno")
  phones.add_child("Samsung")
  
  tv.add_child("Samsung")
  tv.add_child("LG")
  tv.add_child("Hisense")
  
  hp = TreeNode("Hp", laptop)
  dell = TreeNode("Dell", laptop)
  soft = TreeNode("Microsoft", laptop)
  laptop.add_childNode(dell)
  laptop.add_childNode(hp)
  laptop.add_childNode(soft)
  
  hp.add_child("01")
  
  elect.print_tree()
  print(tv.get_level())
  print(tv.size())
  print(hp.size())
  print(elect.size())
  print(elect.search("Samsung"))
  ceo = TreeNode("Nilupul (CEO)")
  cto = TreeNode("Chinmay (CTO)", ceo)
  hr = TreeNode("Gel (HR Head)", ceo)
  
  hr.add_child("Peter (Recruitment Manager)")
  hr.add_child("Waqas (Policy Manager)")
  
  ih = TreeNode("Vishaw (Infrastructure Head)", cto)
  ih.add_child("Dhaval (Cloud Manager)")
  ih.add_child("Abhijit (App Manager)")
  
  ah = TreeNode("Aamir (Application Head)", cto)
  
  cto.add_childNode(ih)
  cto.add_childNode(ah)
  
  ceo.add_childNode(cto)
  ceo.add_childNode(hr)
  print()
  ceo.print_tree()