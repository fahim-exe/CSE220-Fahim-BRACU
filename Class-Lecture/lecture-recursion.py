# Run This cell Second
class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

class LinkedList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array. head will refer
  #  to the Node that contains the element from a[0]
  #  Else Sets the value of head. head will refer
  #  to the given LinkedList

  # Hint: Use the type() function to determine the data type of a
    self.head = None
    self.tail = None
    #self.count = 0
    if type(a)==list:
      self.head = Node(a[0], None,)
      self.tail = self.head
      #self.count +=1
      
      for i in range(1, len(a)):
        n = Node(a[i], None)
        self.tail.next = n
        self.tail = self.tail.next
        #self.count +=1
    
    elif type(a)== Node:
      temp = a
      self.head = a
      self.tail = temp
      while temp.next!=None:        
        temp = temp.next  
      
  def get_head(self):
    return self.head

  


def fact(number):
    if number==1:
        return 1

    else:
        return number*fact(number-1)

#print(fact(5))


#here fibonacci has 0 is the 0th index and 1 is 1th index and so on
def fibo(number):
    if number==0 or number==1:
        return number
    else:
        return fibo(number-1)+fibo(number-2)

#print(fibo(4))

#recursive sum



#arr = [2,4,6,10, 12]
#l1 = LinkedList(arr)

#head = l1.get_head()

def recur_sum(head):
    if head==None:
        return 0

    else:
        return head.element+recur_sum(head.next)


#print(recur_sum(head))

# length of string with recursion

def lenght(str):
    if str=="":
        return 0
    else:
        return 1+ lenght(str[1:])

s = "abcde"

#print(lenght(s))


# sequetial search  for linked list

def seq_search(head, key):
    if head == None:
        return False
    
    elif head.element == key:
        return True
    else:
        return seq_search(head.next, key)
        
#print(seq_search(head, 10))

#sequential search for array

def seq_search_arr(arr, left, key):
    if left>=len(arr):
        return False
    
    elif arr[left] == key:
        return True

    else:
        return seq_search_arr(arr, left+1, key)

#left = 0

#print(seq_search_arr(arr, left, 12))


#binary search for array
def bin_search(arr, left, right, key):
    if left>right:
        return f"Key not in the array. {False}"

    else:
        mid = int((left+right)/2)

        if arr[mid]==key:
            x = mid
            return f"position : {x}, {True}"
        
        elif key>arr[mid]:
            return bin_search(arr, mid+1, right, key)

        else:
            return bin_search(arr, left, mid-1, key)

arr = [2,4,6,10,12,14,15,17]
left = 0
right = len(arr)-1

print(bin_search(arr, left, right, 20))
