from collections import deque
import random, time, threading

class Queue:
  """
  A queue is an ordered list in which insertions are done at one end (rear) and deletions are done at other end (front). 
  The first element to be inserted is the first one to be deleted. Hence, it is called First in First out (FIFO) or Last in Last out (LILO) list."""
  
  def __init__(self, limit=5):
    self.container = deque()
    self.limit = limit
    
  def enqueue(self, obj):
    if self.size() >= self.limit:
      print("Queue overflow")
      return 
    else:
      self.container.appendleft(obj)
    
  def dequeue(self):
    if self.size() <= 0:
      print("Queue Underflow")
      return 
    else:
      return self.container.pop()
    
  def rear(self):
    if self.size() <= 0:
      return "Sorry the queue is empty"
    return self.container[0]
    
  def front(self):
    if self.size() <= 0:
      return "Sorry the queue is empty"
    return self.container[-1]
    
  def is_empty(self):
    return self.size() <= 0
    
  def size(self):
    return len(self.container)
    
  def remove(self, obj):
    self.container.remove(obj)
    
  def get_index(self, obj):
    return self.container.index(obj)
    
    
    
# Simple Circular Array Implementation
class Queue_2:
  """
  A queue is an ordered list in which insertions are done at one end (rear) and deletions are done at other end (front). 
  The first element to be inserted is the first one to be deleted. Hence, it is called First in First out (FIFO) or Last in Last out (LILO) list."""
  
  def __init__(self, limit=5):
    self.que = []
    self.front = None 
    self.rear = None 
    self.limit = limit 
    self.size = 0 
    
  def enqueue(self, obj):
    if self.size >= self.limit:
      return print("Queue Overflow")
    else:
      self.que.append(obj)
    if self.front == None:
      self.front = self.rear = 0 
    else:
      self.rear = self.size
    self.size += 1 
    print(f"Queue after enque: {self.que}")
    
  def dequeue(self):
    if self.size <= 0:
      return print("Queue underflow")
    else:
      front = self.queFront()
      self.que.remove(front)
      self.size -= 1 
      if self.size == 0:
        self.rear = self.front = None 
      else:
        self.rear -= 1
      print(f"Queue after dequeue: {self.que}")
    
  def queFront(self):
    if self.front == None:
      return "Sorry, the queue is empty"
    else:
      return self.que[self.front]
      
  def queRear(self):
    if self.rear == None:
      return "Sorry the queue is empty"
    else:
      return self.que[self.rear]
      
      
# Linked List Implementation of queue
class Node:
  def __init__(self, value=None, nxt=None, prev=None):
    self.value = value 
    self.next = nxt 
    self.prev = prev 
    
  def __repr__(self):
    nval = self.next and self.next.value or None
    pval = self.prev and self.prev.value or None 
    return f"[{repr(pval)}, {self.value}, {repr(nval)}]"


class Queue_3(object):
  """
  A queue is an ordered list in which insertions are done at one end (rear) and deletions are done at other end (front). 
  The first element to be inserted is the first one to be deleted. Hence, it is called First in First out (FIFO) or Last in Last out (LILO) list."""
  
  def __init__(self, limit=5):
    self.front = None
    self.rear = None 
    self.limit = limit
    
  def to_list(self):
    l = []
    if self.front == None:
      return l 
    else:
      curr_node = self.rear 
      while curr_node:
        l.append(curr_node.value)
        curr_node = curr_node.next
    return l
    
  def enqueue(self, obj):
    if len(self.to_list()) >= self.limit:
      print("Queue Overflow")
      return
    elif self.front == None:
      self.front = Node(obj)
      self.rear = self.front 
    else:
      curr_rear = self.rear
      curr_rear.prev = Node(obj)
      self.rear = curr_rear.prev
      self.rear.next = curr_rear
      
  def dequeue(self):
    if len(self.to_list()) <= 0:
      print("Queue underflow")
      return 
    else:
      front = self.front 
      if self.front != self.rear:
        self.front = front.prev
        self.front.prev = front.prev.prev
      else:
        self.front = None
      return front.value
    
    
    
    
    
if __name__=="__main__":
  que = Queue()
  que.container
  que.enqueue("first") 
  que.enqueue("sccond") 
  que.enqueue("third") 
  que.enqueue("fourth") 
  que.enqueue("fifth") 
  que.enqueue("sixth") 
  print(que.container)
  print("rear: " + que.rear())
  print("front: " + que.front())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.is_empty())
  
  print()
  print()
  print()
  
  que = Queue_3()
  que.enqueue("first") 
  que.enqueue("second") 
  que.enqueue("third") 
  que.enqueue("fourth") 
  print(que.to_list())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
  print(que.dequeue())
