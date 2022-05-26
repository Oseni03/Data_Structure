from collections import deque
import random, time, threading

class Queue:
  def __init__(self):
    self.container = deque()
    
  def enqueue(self, obj):
    self.container.appendleft(obj)
    
  def dequeue(self):
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
    
    
# Exercise
def place_order(food_list):
  order = Queue()
  for i in range(10):
  #while True:
    food = random.choice(food_list)
    order.enqueue(food)
    print(f"Order placed---> {food}")
    time.sleep(0.5)
  return order
  
def serve_order(orders):
  while not orders.is_empty():
    print(f"Order served--->{orders.dequeue()}")
    time.sleep(2)
    
    
place=["meat pie", "samosa", "egg buns", "fried rice", "jollof rice"]
#serve_order(orders)

t1 = threading.Thread(target=place_order, args=[place])
t2 = threading.Thread(target=serve_order, args=[place_order(place)])

t1.start()
t1.join()
time.sleep(1)
t2.start()
t2.join()

