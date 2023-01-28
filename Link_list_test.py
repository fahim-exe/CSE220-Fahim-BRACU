class Node:
  def __init__(self, value):
      self.next = None
      self.prev = None
      self.val = value

class Double_Link_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def add_node(self, value):
    node = Node(value)
    if self.tail is None:
      self.head = node
      self.tail = node
      self.size += 1
    else:
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
      self.size +=1


  def __str__(self):
    values = []
    node = self.head 
    while node is not None:
      values.append(node.val)
      node = node.next
    return f"[{','.join(str(val) for val in values)}]"
  
  def __remove_node(self, node):
    if node.prev is None:
      self.head = node.next
    else:
      node.prev.next = node.next

    if node.next is None:
      self.tail = node.prev
    else:
      node.next.prev = node.prev
  
   
  def remove_item(self, value):
    node = self.head
    while node is not None:
      if node.val==value:
        self.__remove_node(node)
        break
      node=node.next
    self.size -=1
my_list = Double_Link_List()
my_list.add_node(1)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(1)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(5)
my_list.add_node(1)
my_list.add_node(5)
my_list.add_node(5)

my_list.add_node(2)
print(my_list)

my_list.remove_item(5)
print(my_list)
