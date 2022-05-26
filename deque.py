from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()
    
  def push(self, obj):
    self.container.append(obj)
    
  def pop(self):
    return self.container.pop()
    
  def peek(self):
    return self.container[-1]
    
  def is_empty(self):
    return False if self.container else True
    
  def size(self):
    return len(self.container)
    
  def remove(self, obj):
    self.container.remove(obj)
    
  def get_index(self, obj):
    return self.container.index(obj)
    
# Exercise 1
def reverse_string(strings):
  """ This func return the reverse of a string entered"""
  reverse = Stack()
  for i in strings:
    reverse.push(i)
  new = ""
  while not reverse.is_empty():
    val = reverse.pop()
    new += val
  return new

# Exercise 2
def is_balanced(string):
  """ This func checks if parenthesis is balanced or not"""
  b = Stack()
  balance = 0
  for s in string:
    if s in  ["(", "{", "["]:
      b.push(s)
    else:
      if b.is_empty():
        balance = 0 
      else:
        c = b.pop()
        if c == "(" and s == ")" or c == "{" and s == "}" or c == "[" and s == "]":
          balance = 1 
        else:
          balance = 0 

  return balance
      


if __name__=="__main__":
  # colors = Stack()
  # colors.push("Vermillion")
  # colors.push("Sap Green")
  # colors.push("Cadmium Yellow Light")
  # print(colors.size())
  # print(colors.pop())
  # print(colors.pop())
  # print(colors.is_empty())
  # print(colors.size())
  # print(colors.pop())
  # print(colors.size())
  print(reverse_string("hello there"))
  print(is_balanced("({}{())}()"))