class BinaryTreeNode: 
  def __init__(self, data): 
    self.data = data 
    self.left = None 
    self.right = None 
    
  def __repr__(self):
    return f"{self.data}"
    
  def add_child(self, data):
    if self.data == data:
      return
    
    elif data > self.data:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinaryTreeNode(data)
        
    elif data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinaryTreeNode(data)
        
        
  def preorder_traversal(self):
    result = []
    result.append(self.data)

    if self.left:
      result += self.left.inorder_traversal()
    
    if self.right:
      result += self.right.inorder_traversal()
    
    # stack= []
    # stack.append(self) 

    # while stack:
    #   node = stack.pop() 
    #   result.append(node.data) 
    #   if node.right: stack.append(node.right)
    #   if node.left: stack.append(node.left)
    return result 
    
    
  def inorder_traversal(self):
    element = []
    
    if self.left:
      element += self.left.inorder_traversal()
    
    element.append(self.data)
    
    if self.right:
      element += self.right.inorder_traversal()
    return element


  def postorder_traversal(self):
    element = []

    if self.right:
      element += self.right.inorder_traversal()
    
    if self.left:
      element += self.left.inorder_traversal()
      
    element.append(self.data)
    return element


  def get_size(self):
    element = 1

    if self.right:
      element += self.right.get_size()
    
    if self.left:
      element += self.left.get_size()
      
    return element 


  def search(self, val):
    if val == self.data:
      return True 
      
    else:
      if val < self.data:
        if self.left:
          temp = self.left.search(val)
          if temp:
            return temp
        else:
          return False 
          
      if val > self.data:
        if self.right:
          temp = self.right.search(val)
          if temp:
            return temp
        else:
          return False 
    return False 
        
        
  def get_max(self):
    result = 0
    if self.data > result:
      result = self.data

    if self.left:
      result = self.left.get_max()
    
    if self.right:
      result = self.right.get_max()
    return result
        
        
  def get_min(self):
    if self.left == None:
      return self.data 
    return self.left.get_min()
    
  def get_deepest(self):
    node = None
    if self.data:
      node = self
    if self.left:
      node = self.left.get_deepest()
    if self.right:
      node = self.right.get_deepest()
    return node 
    
    
  def delete(self, data):
    if self.data == data:
      if self.right == None and self.left == None:
        return None 
      if self.right and self.left == None:
        return self.right 
      if self.left and self.right == None:
        return self.left
      
      m = self.right.get_min()
      self.data = m 
      self.right = self.right.delete(m)
        
        # OR
        
      # elif self.left:
      #   m = self.left.get_max()
      #   self.data = m 
      #   self.left = self.left.delete(m)
      #   return self 
      
    if data < self.data:
      if self.left:
        self.left = self.left.delete(data)
    if data > self.data:
      if self.right:
        self.right = self.right.delete(data)
    return self
    
  
  def BST_check(self):
    if self.left != None and self.left.get_max() >= self.data:
      return False 
    if self.right != None and self.right.get_min() <= self.data:
      return False 
    return True
      
  
      
        
if __name__=="__main__":
  tree = BinaryTreeNode(10)
  tree.add_child(7)
  tree.add_child(2)
  tree.add_child(6)
  tree.add_child(15)
  tree.add_child(34)
  tree.add_child(12)
  tree.add_child(28)
  tree.add_child(1)
  tree.add_child(3)
  tree.add_child(9)
  print(tree.preorder_traversal())
  print(tree.inorder_traversal())
  print(tree.postorder_traversal())
  print(tree.search(3))
  print(tree.get_max())
  print(tree.get_min())
  print(tree.get_size())
  print(tree.get_deepest())
  print(tree.delete(10))
  print(tree.preorder_traversal())
  print(tree.search_2(39))
  print(tree.BST_check())
  