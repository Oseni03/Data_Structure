import os 

class Tree:
  def __init__(self, dir=os.getcwd()):
    self.dir = dir
    self.files = os.listdir(dir)
    self.level = 0
    self.d = os.getcwd()
    
  def printt(self):
    space = " " * self.level 
    prefix = space + "|--" if not self.d == self.dir else ""
    
    for file in self.files:
      print(prefix + file)
      self.level = self.level + 1
      if os.path.isdir(file):
        # self.files = os.listdir(file)
        # path = os.path.realpath(file)
        # self.d, _ = os.path.split(path)
        new = self.dir + f'/{file}'
        new = Tree(new)
        new.printt()
  
class TreeNode:
  def __init__(self, dir=os.getcwd(), parent=None):
    self.data = dir 
    self.parent = parent 
    self.children = []
    if os.path.isdir(self.data):
      for file in os.listdir(self.data):
        self.add_child(file)
    
  def print_tree(self):
    space = " " * self.get_level() * 3
    prefix = space + "|--" if self.parent else "|--"
    
    for child in self.children:
      print(prefix + child.name())
      if os.path.isdir(child.data):
      #if child.children:
        new = child.parent.data + f'/{child.name()}'
        new = TreeNode(new, self)
        #self.add_childNode(new)
        new.print_tree()
        #child.print_tree()
      else:
        continue
          
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
    
  def name(self):
    _, name = os.path.split(self.data)
    return name
    
  
if __name__=="__main__":
  # curdir = os.getcwd()
  # tree = Tree()
  # tree.printt()
  # curdir = os.getcwd()
  tree = TreeNode()
  print(tree.print_tree())