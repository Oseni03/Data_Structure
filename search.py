# Linear Search
def linearSearch(numberList, value):
  for idx, element in enumerate(numberList):
    if element == value:
      return idx
  return -1
  
def BinarySearch(numberList, value): 
  low = 0 
  high = len(numberList)-1
  print(high)
  mid = 0
  
  while low <= high:
    mid = (low+high)//2
    #print(mid)
    if numberList[mid] == value:
      return mid 
    elif numberList[mid] > value:
      high = mid - 1
    elif numberList[mid] < value:
      low = mid + 1
    else:
      return mid
  return -1
  
# def recursiveBinarySearch(numberList, value, low=0, high = -1):
#   if not numberList: return -1 
#   if(high == -1): high = len(numberList) - 1
#   if low == high:
#     if numberList[low] == value:
#       return low 
#     else:
#       return -1
  
#   mid = low + (high-low)//2
#   #print(mid)
#   if numberList[mid] == value:
#     return mid 
#   if numberList[mid] < value:
#     return recursiveBinarySearch(numberList, value, mid + 1, high)
#   elif numberList[mid] > value:
#     return recursiveBinarySearch(numberList, value, low, mid - 1)

#   return recursiveBinarySearch(numberList, value, low, high)
    
    
def recursiveBinarySearch(numberList, value, left_index, right_index):
  if right_index < left_index:
    return -1 
  
  mid_index = (left_index + right_index) // 2 
  if mid_index >= len(numberList) or mid_index < 0:
    return -1
    
  mid_value = numberList[mid_index]
  
  if mid_value == value:
    return mid_index
    
  if mid_value < value:
    left_index = mid_index + 1
  else:
    right_index = mid_index - 1
    
  return recursiveBinarySearch(numberList, value, left_index, right_index)
  
  
if __name__=="__main__":
  A= [534,246,933,127,277,321,454,565,220]
  print(linearSearch(A, 220))
  print(recursiveBinarySearch(A, 534, 0, len(A)))