class HashTable:
  def __init__(self):
    self.Max = 100 
    self.arr = [[] for i in range(self.Max)]
    
  def get_hash(self, key):
    hash = 0 
    for char in key:
      hash += ord(char)
    return hash % self.Max
    
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    found = False 
    for idx, element in enumerate(self.arr[h]):
      if len(element) == 2 and element[0] == key:
        self.arr[h][idx] = (key, value)
        found = True 
        break
    if not found:
      self.arr[h].append((key, value))
    
  def __getitem__(self, key):
    h = self.get_hash(key)
    if self.arr[h]:
      for element in self.arr[h]:
        if element[0] == key:
          return element[1]
    else:
      return None
    
  def __delitem__(self, key):
    h = self.get_hash(key)
    for idx, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]
        
  # def repeatedChar(self, string):
  #   size = len(string)
  #   count = [0] * (256)
  #   for i in range(size):
  #     if count[ord(str(i))]==1:
  #       print(str(i))
  #       break 
  #     else: 
  #       count[ord(str(i))] += 1 
  #   if(i==size): 
  #     print("No Repeated Characters")
  #   return 0
  

# Implementing Separate Chaining Collision
class HashTable_2:
  def __init__(self):
    self.Max = 10 
    self.arr = [None for i in range(self.Max)]
    # self.slots = [None] * self.size 
    # self.data * [None] * self.size
    
  def get_hash(self, key):
    hash = 0 
    for char in key:
      hash += ord(char)
    return hash % self.Max
    
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    print(f"{key}--{h}")
    if self.arr[h] == None:
      self.arr[h] = (key, value)
    else:
      if self.arr[h] != None and self.arr[h][0] == key:
        self.arr[h] = (key, value) 
      else:
        newh = self.rehash(h)
        while self.arr[newh] != None:
          newh = self.rehash(newh)
        if self.arr[newh] == None:
          self.arr[newh] = (key, value)
        else:
          if self.arr[newh] != None and self.arr[newh][0] == key:
            self.arr[newh] = (key, value)  
        
  def rehash(self, oldhash): 
    return (oldhash + 1) % self.Max
    
  def __getitem__(self, key):
    h = self.get_hash(key)
    data = None 
    found = False 
    position = h
    while self.arr[position] != None and not found:
      if self.arr[position][0] == key:
        data = self.arr[position][1]
        break
      else:
        position = self.rehash(position)
        if position == h:
          break
    return data

    
  def __delitem__(self, key):
    h = self.get_hash(key)
    found = False 
    position = h
    while self.arr[position] != None and not found:
      if self.arr[position][0] == key:
        self.arr[position] = None
        break
      else:
        position = self.rehash(position)
        if position == h:
          break

    
    
if __name__=="__main__":
  t = HashTable()
  t["first"]= 1
  t["first"]= 5
  t["second"] = 2
  print(t.arr)
  print(t["second"])
  del t["second"]
  print(t.arr)
  print(t["second"])
  print()
  print()
  H = HashTable_2()
  H["first"]= 1
  H["first"]= 5
  H["second"] = 2
  H["third"] = 4
  H["fourth"] = 2
  H["fifth"] = 6
  H["sixth"] = 9
  H["seventh"] = 10
  print(H.arr)
  print(H["fifth"])
  print(H["third"])
  del H["second"]
  print(H.arr)
  print(H["second"])
  