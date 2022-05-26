class Node(object):
  def __init__(self, value=None, nxt=None ):
    self.value = value
    self.next = nxt

  def __repr__(self):
    nval = self.next and self.next.value or None
    return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):
  def __init__(self):
    self.head = None
    self.end = None

  def to_list(self):
    l = []
    if self.head is None:
      return l

    else:
      node = self.head
      while node:
        l.append(node.value)
        node = node.next
      return l

  def push(self, obj):
    """Appends a new value on the end of the list."""
    if self.head == None:
      self.head = Node(obj, None) 
      self.end = self.head
      return
      
    else:
      self.end.next = Node(obj) 
      self.end = self.end.next
    
  def insert_values(self, data_list):
    """This receive a list of data as an argument create a new list out of it"""
    self.head = None 
    for data in data_list:
      self.push(data)

  def pop(self):
    """Removes the last item and returns it."""
    all = self.to_list()
    
    itr = self.head
    if len(all) > 1:
      while itr:
        if itr.value == all[-2]:
          itr.next = None 
          break
        itr = itr.next
      return all[-1]
    elif len(all) == 1:
      #print(all)
      self.head = None 
      return all[0] # or self.head.value
    else:
      return None

  def shift(self, obj):
    """Another name for push. It pushed the object to the first/beginning"""
    if self.head == None:
      self.head = Node(obj)
      self.end = self.head
      
    node = Node(obj, self.head)
    self.head = node
      

  def unshift(self):
    """Removes the first item and returns it."""
    if self.head == None:
      return None 
    
    l = self.head
    self.head = self.head.next
    return l.value

  def remove(self, obj):
    """Finds a matching item and removes it from the list."""
    all=self.to_list()
    if obj not in all:
      return "Object not found!"
    
    itr = self.head
    while itr:
      if itr.value == obj:
        self.head = self.head.next
        break
      elif itr.next.value == obj:
        itr.next = itr.next.next
        break
      itr = itr.next
    return
      
        
  def first(self):
    """Returns a reference to the first item, does not remove."""
    return self.head.value

  def last(self):
    """Returns a reference to the last item, does not remove."""
    return self.end.value

  def count(self):
    """Counts the number of elements in the list.""" 
    all = self.to_list()
    return len(all)
      

  def get(self, index):
    """Get the value at index."""
    if index < 0 or index >= self.count():
      raise Exception("Invalid index")
    
    if index == 0:
      return self.head.value
      
    counts = 0
    itr = self.head
    while itr:
      if index == counts:
        return itr.value
      itr = itr.next
      counts += 1
      

  def insert_at(self, index, obj):
    """Insert object at index."""
    if index < 0 or index >= self.count():
      return None
    elif index == 0:
      self.shift(obj)
      
    counts = 0
    itr = self.head
    while itr:
      if counts == index - 1:
        node = Node(obj, itr.next)
        itr.next = node 
        break
      itr = itr.next
      counts += 1
      

  def remove_at(self, index):
    """Remove the value at index."""
    if index < 0 or index >= self.count():
      raise Exception("Invalid index")
    
    if index == 0:
      self.head = self.head.next
      
    counts = 0
    itr = self.head
    while itr:
      if index == counts - 1:
        itr.next = itr.next.next
        break
      itr = itr.next
      counts += 1


  def dump(self, mark):
    """Debugging function that dumps the contents of the list."""
    pass


  def to_string(self):
    """Represent all the data in the list in a string accordingly."""
    all = ""
    itr =self.head
    while itr:
      all += itr.value + " --> "
      itr = itr.next
    all += "None"
    return all


  def insert_after_value(self, data_after, obj):
    # search for first occurrence of data_after
    # Now insert the obj after the data_after
    
    itr = self.head 
    while itr:
      if itr.value == data_after:
        itr.next = Node(obj, itr.next)
      itr = itr.next


if __name__=="__main__":
  colors = SingleLinkedList()
  colors.push("Vermillion")
  colors.push("Sap Green")
  colors.push("Cadmium Yellow Light")
  print(colors.to_string())
  colors.insert_after_value("Sap Green", "New")
  print(colors.to_string())
  colors.insert_after_value("Cadmium Yellow Light", "second")
  print(colors.to_string())
