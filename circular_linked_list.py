class Node(object):
  def __init__(self, value=None, nxt=None ):
    self.value = value
    self.next = nxt

  def __repr__(self):
    nval = self.next and self.next.value or None
    return f"[{self.value}:{repr(nval)}]"


class CircularLinkedList(object):
  def __init__(self):
    self.head = None
    self.end = None 
    
  def count(self):
    curr_node = self.head
    if curr_node == None:
      return 0
    else:
      count = 1
      curr_node = curr_node.next
      while curr_node != self.head:
        curr_node = curr_node.next
        count += 1
      return count

  def to_list(self):
    l = []
    if self.head == None:
      return l 
    else:
      l.append(self.head.value)
      curr_node = self.head.next
      while curr_node != self.head:
        l.append(curr_node.value)
        curr_node = curr_node.next
      return l

  def push(self, obj):
    if self.head == None:
      self.shift(obj)
    else:
      self.end.next = Node(obj, self.head)
      self.end = self.end.next
    
  def shift(self, obj):
    if self.head == None:
      node = Node(obj, Node(obj))
      self.head = node 
      self.end = self.head
      self.end.next = self.head
    else:
      self.head = Node(obj, self.head)
      self.end.next = self.head
      
  def pop(self):
    if self.head == None:
      print("List is empty")
      
    prev = self.head
    itr = self.head
    while itr.next != self.head:
      prev = itr 
      itr = itr.next
    prev.next = self.head
    self.end = prev 
    return itr.value
      
  def unshift(self):
    """Removes the first item and returns it."""
    if self.head == None:
      return None 
    else:
      head = self.head
      self.end.next = head.next
      self.head = head.next
      return head.value
      
      
if __name__=="__main__":
  colors = CircularLinkedList()
  colors.push("Vermillion")
  colors.push("sugar")
  colors.push("Sap Green")
  colors.push("Cadmium Yellow Light")
  colors.push("Cadmium green Light")
  print(colors.count())
  print(colors.to_list())
  print(colors.unshift())
  print(colors.to_list())
  print(colors.unshift())
  print(colors.unshift())
  print(colors.to_list())
  