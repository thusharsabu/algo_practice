
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def create_list(self, arr):
    if self.head == None:
      current_node = Node(arr[0])
      self.head = current_node
    else:
      current_node = self.get_tail()
      current_node.next = Node(arr[0])
      current_node = current_node.next
    
    for element in arr[1:]:
      current_node.next = Node(element)
      current_node = current_node.next
    print("Created Success fully")

  def print_linked_list(self):
    current_node = self.head
    while current_node is not None:
      print(str(current_node.value)+ " ->", end='')
      current_node = current_node.next
  
  def to_array(self):
    arr = []
    current_node = self.head
    while current_node is not None:
      arr.append(current_node.value)
      current_node = current_node.next
    return arr

  def get_tail(self):
    current_node = self.head
    while current_node.next is not None:
      current_node = current_node.next
    return current_node