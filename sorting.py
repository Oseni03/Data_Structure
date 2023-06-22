def bubble_sort(List):
  size = len(List)
  
  for i in range(size - 1):
    swapped = False
    for j in range(size-1-i):
      if List[j] > List[j+1]:
        tmp = List[j]
        List[j] = List[j+1]
        List[j+1] = tmp 
        swapped = True 
    if not swapped:
      break
  return List


def new_bubble(List):
  n = len(List)
  for _ in range(n):
    swapped = False 
    for i in range(1, len(List)):
      if List[i-1] > List[i]:
        List[i-1], List[i] = List[i], List[i-1]
        swapped = True
    if not swapped:
      break 
  return List


def dict_bubble_sort(List, key):
  size = len(List)
  
  for i in range(size - 1):
    swapped = False 
    for j in range(size-1-i):
      print(f"SAMPLE: {List[j]}")
      print()
      if List[j][key] > List[j+1][key]:
        tmp = List[j]
        List[j] = List[j+1]
        List[j+1] = tmp 
        swapped = True 
    if not swapped:
      break
  return List
  
  
def selection_sort(List): 
  for i in range(len(List)-1): 
    least = i 
    
    for k in range(i + 1, len(List)): 
      if List[k] < List[least]: 
        least = k 
        
    if least != i:
      List[i], List[least] = List[least], List[i]
  return List
  
  
def dict_selection_sort(List, keys): 
  for i in range(len(List)-1): 
    least = i 
    
    for i in range(len(keys)):
      for k in range(i + 1, len(List)): 
        if List[k][keys[i]] < List[least][keys[i]]:
          least = k 
          
      if least != i:
        List[i], List[least] = List[least], List[i]
    List = List
  return List


def insertion_sort(List):
  for i in range(1, len(List)):
    curr = List[i]
    idx = i 
    while idx > 0 and curr < List[idx-1]:
      List[idx] = List[idx-1]
      idx = idx - 1
    List[idx] = curr
  return List


def shell_sort(List):
  gap = len(List)//2
  while gap:
    for i in range(gap, len(List)):
      curr = List[i]
      idx = i 
      while idx >= gap and curr < List[idx-gap]:
        List[idx] = List[idx-gap]
        idx = idx - gap
      List[idx] = curr
    gap = gap//2
  return List

# Not working yet
def dup_shell_sort(List):
  size = len(List)
  gap = size//2
  while gap:
    for i in range(gap, len(List)):
      if i < len(List):
        curr = List[i]
        idx = i 
        while idx >= gap and curr <= List[idx-gap]:
          if List[idx-gap] == curr:
            del List[idx-gap]
            print(List)
          else:
            List[idx] = List[idx-gap]
            idx = idx - gap 
        List[idx] = curr
    gap = gap//2
  return List


def merge_sort(List, key=None):
  if len(List) <= 1:
    return List
  mid = len(List)//2
  left = List[:mid]
  right = List[mid:]
  
  merge_sort(left, key)
  merge_sort(right, key)
  merge(left, right, List, key)


def merge(left, right, List, key):
  i = j = k = 0 
  
  if key != None:
    while i < len(left) and j < len(right):
      if left[i][key] <= right[j][key]:
        List[k] = left[i]
        i += 1
        k += 1
      else:
        List[k] = right[j]
        j += 1
        k += 1
    while i < len(left):
      List[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      List[k] = right[j]
      j += 1
      k += 1
  
  else:
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        List[k] = left[i]
        i += 1
        k += 1
      else:
        List[k] = right[j]
        j += 1
        k += 1
    while i < len(left):
      List[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      List[k] = right[j]
      j += 1
      k += 1
  
  
def partition(List, start, end):
  pivot_idx = start
  pivot = List[pivot_idx]
  
  while start < end and start < len(List):
    while List[start] <= pivot:
      start += 1 
    
    while List[end] > pivot:
      end -=1 
    
    if start < end:
      List[start], List[end] = List[end], List[start]
      
  List[pivot_idx], List[end] = List[end], List[pivot_idx]
  return end
  
  
def quick_sort(List, start, end):
  if start < end:
    pivot = partition(List, start, end)
    quick_sort(List, start, pivot-1)
    quick_sort(List, pivot+1, end)
  
  
def mysort(List):
  pivot_idx = 0
  while pivot_idx <= len(List):
    for idx in range(pivot_idx+1, len(List)):
      if List[idx] <= List[pivot_idx]:
        temp = List[pivot_idx]
        List[pivot_idx] = List[idx]
        List[idx] = temp 
    pivot_idx += 1
  return List
      
      
if __name__=="__main__":
  List = [65,21,54,2,90,43,11,23,21,6,7]
  
  # List = [
  #   {"name": "Oseni Omowunmi", "transaction_cost": 200, "device": "Nokia"},
  #   {"name": "Oseni Ayomide", "transaction_cost": 5000, "device": "Iphone"},
  #   {"name": "Oseni Ibrahim", "transaction_cost": 2500, "device": "Samsung"},
  #   {"name": "Oseni Aliya", "transaction_cost": 50, "device": "Toy"}
  #   ]
  #print(dict_bubble_sort(List, "name"))
  #a = dict_selection_sort(List, ["transaction_cost", "device"])
  # merge_sort(List)
  # for a in List:
  #   print(a)
  print(List)
  quick_sort(List, start=0, end=len(List)-1)
  print(List)
  