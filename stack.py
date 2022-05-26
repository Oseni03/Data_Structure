class Node(object):
  def __init__(self, value=None, nxt=None ):
    self.value = value
    self.next = nxt

  def __repr__(self):
    nval = self.next and self.next.value or None
    return f"[{self.value}:{repr(nval)}]"


class Stack(object):
  def __init__(self):
    self.top = None

  def push(self, obj):
    """Pushes a new value to the top of the stack."""
    if self.top == None:
      self.top = Node(obj)
    else:
      self.top = Node(obj, self.top)
    
  def pop(self):
    """Pops the value that is currently on the top of the stack."""
    if self.top == None:
      return None 
    else:
      top = self.top
      self.top = top.next
      return top.value
    
  def top(self):
    """Returns a reference to the first item, does not remove."""
    return self.top.value
    
  def size(self):
    """Counts the number of elements in the stack."""
    if self.top == None:
      return 0
    else:
      count = 1
      top = self.top
      while top.next != None:
        count += 1
        top = top.next
      return count
    
  def dump(self, mark="----"):
    """Debugging function that dumps the contents of the stack."""
    

# Simple Array I mplementation
class Stack_2(object): 
  def __init__(self, Limit=10): 
    self.stk = []
    self.limit = Limit 

  def is_empty(self): 
    return len(self.stk) <= 0 
    
  def push(self, item): 
    if len(self.stk) >= self.limit: 
      print ('Stack Overflow!')
    else: 
      self.stk.append(item) 
      print ('Stack after Push',self.stk)

  def pop(self): 
    if len(self.stk) <= 0: 
      print ('Stack Underflow!')
      return 0 
    else: 
      return self.stk.pop()
      
  def peek(self): 
    if len(self.stk) < 0: 
      print ('Stack Underflow')
      return 0 
    else: 
      return self.stk[-1]
      
  def size(self): 
    return len(self.stk)
    
    
    
if __name__=="__main__":
  colors = Stack()
  colors.push("Vermillion")
  colors.push("Sap Green")
  colors.push("Cadmium Yellow Light")
  print(colors.size())
  print(colors.pop())
  print(colors.pop())
  print(colors.size())
  print(colors.pop())
  print(colors.size())