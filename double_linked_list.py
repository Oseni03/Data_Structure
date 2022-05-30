class Node:
  def __init__(self, value=None, nxt=None, prev=None):
    self.value = value 
    self.next = nxt 
    self.prev = prev 
    
  def __repr__(self):
    nval = self.next and self.next.value or None
    pval = self.prev and self.prev.value or None 
    return f"[{repr(pval)}, {self.value}, {repr(nval)}]"
    
    
class DoubleLinkedList(object):
  def __init__(self):
    self.head = None
    self.end = None
    
  def to_list(self):
    l = []
    if self.head is None:
      return l

    node = self.head
    #l.append(self.head.prev)
    
    while node:
      l.append(node.value)
      node = node.next
    #l.append(None)
    return l

  def push(self, obj):
    """Appends a new value on the end of the list."""
    if self.head == None:
      self.head = Node(obj) 
      self.end = self.head
      return
      
    self.end.next = Node(obj, None, self.end) 
    self.end = self.end.next

  def pop(self):
    """Removes the last item and returns it."""
    if self.end == self.head:
      last = self.end.value
      self.head = None
    
    else:
      last_node = self.end
      prev_node = self.end.prev

      prev_node.next = None
      self.end = prev_node
      return last_node.value
        
    
    
  def shift(self, obj):
    """Actually just another name for push. It pushed the object to the first/beginning."""
    if self.head == None:
      self.head = Node(obj)
      self.end = self.head 
      
    node = Node(obj, self.head, None)
    self.head = node

  def unshift(self):
    """Removes the first item (from begin) and returns it."""
    if self.head == None:
      return None 
    elif self.head.next == None:
      l = self.head.value
      self.head = None
      return l
    
    else:
      l = self.head
      new_head = self.head.next
      new_head.prev = None
      self.head = new_head
      return l.value
    
  def detach_node(self, node):
    """You'll need to use this operation sometimes, but mostly inside remove(). 
    It should take a node, and detach it from the list, whether the node is at the front, end, or in the middle."""

  def remove(self, obj):
    """Finds a matching item and removes it from the list."""
    all = self.to_list()
    if obj not in all:
      return None 
    elif self.head.value == obj:
      new_head = self.head.next
      new_head.prev = None 
      self.head = new_head
      return
    
    else:
      prev_node = self.head
      curr_node = self.head
      while curr_node:
        if curr_node.value == obj:
          prev_node.next = curr_node.next
          break 
        prev_node=curr_node
        curr_node = curr_node.next

  def first(self):
    """Returns a reference to the first item, does not remove."""
    return self.head.value

  def last(self):
    """Returns a reference to the last item, does not remove."""
    return self.end.value

  def count(self):
    """Counts the number of elements in the list."""
    return len(self.to_list())

  def get(self, index):
    """Get the value at index."""
    if index < 0 or index >= self.count():
      return None 
    elif index == 0:
      return self.head.value
      
    counts = 0
    itr = self.head 
    while itr:
      if counts == index:
        return itr
      counts += 1
      itr = itr.next
      
  def insert_values(self, data_list):
    """This receive a list of data as an argument create a new list out of it"""
    for data in data_list:
      self.push(data)
      
  def insert_at(self, index, obj):
    """Insert object at index."""
    if index < 0 or index >= self.count():
      return None
    elif index == 0:
      self.shift(obj)
      return 
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        node = Node(obj, itr.next, itr)
        itr.next = node
        break
      count += 1
      itr = itr.next
      
  def remove_at(self, index):
    """Remove the value at index."""
    temp = self.get(index)
    
    if index == 0:
      self.unshift()
    elif index > self.count() - 1:
      raise ValueError("Invalid index")
    else:
      temp.prev.next = temp.next
      if temp.next != None:
        temp.next.prev = temp.prev
      temp = None
    
      
  def print_forward(self):
    """This print list in forward direction"""
    l=[]
    if self.head is None:
      return l 
    
    itr = self.head 
    while itr:
      l.append(itr.value)
      itr = itr.next
    return l
    
  def print_backward(self):
    """This print list in backward direction"""
    l=[]
    if self.end is None:
      return l 
    
    itr = self.end 
    while itr:
      l.append(itr.value)
      itr = itr.prev
    return l

  def dump(self, mark):
    """Debugging function that dumps the contents of the list."""
    
if __name__=="__main__":
  colors = DoubleLinkedList()
  colors.push("Vermillion")
  colors.push("Sap Green")
  colors.push("Cadmium Yellow Light")
  colors.push("dark green")
  print(colors.to_list())
  print(colors.print_backward())
  #colors.remove("dark green")
  #print(colors.to_list())
  

  