class Array:
    def __init__(self, src):
        array = self.create_arr(src)
        self.array = array
  

    
    def create_arr(self, src):
        length = len(src)
        
        arr = [None]*length
        for i in range(length):
            arr[i] = src[i]

        return arr


    def leftshift(self):
        
        for i in range(1, len(self.array)):
            self.array[i-1]=self.array[i]
        last_idx = -1
        self.array[last_idx] =None    
        
        self.array = self.array
        return self.array


    def rightshift(self):
        
        for i in range(len(self.array)-1, 0, -1):
            self.array[i]=self.array[i-1]
        
        self.array[0] =None    
        self.array = self.array
        return self.array



'''arr = [1,2,3,4,5]
array1 = Array(arr)
array2 = Array(arr)
print(array1.leftshift())
print(array2.rightshift())
'''

def right_rotate(arr):
    temp = arr[-1]

    for i in range(len(arr)-1, -1, -1):
        arr[i]=arr[i-1]

    arr[0] = temp

    print(arr)


def insert(arr, element, size, index):
    if size==len(arr):
        return f"No space Left!!!!"

    for i in range(size, index-1):
        arr[i] = arr[i-1]

    arr[index] = element

    print(arr)


'''arr = [1,2,3,4,5, None, None, None]
print(arr)
insert(arr, 100, 5, 2)
'''

def remove(arr, index, size):
    for i in range(index+1, size):
        arr[i-1]=arr[i]
    arr[-1] = None
    print(arr)

'''arr = [1,2,3,4,5]
remove(arr, 1, 5)
'''
'''
arr = [1,2,3,4,5]
right_rotate(arr)'''


def forward_iteration(arr, start):
    k = start
    for i in range(len(arr)):
        print(arr[k])
        k = (k+1)%len(arr)


arr = [1,2,None, None, 3, 4,5,6,7]

#forward_iteration(arr, 4)

def backward_iteration(arr, start, size):
    k = (start+size-1)%len(arr)
    
    for i in range(size):
        print(arr[k])
        k = k-1
        if k==-1:
            k = len(arr)-1
    
#backward_iteration(arr, 4, 7)

def linearization(arr, start, size):
    lin_arr = [None]*size
    k = start
    for i in range(size):
        lin_arr[i] = arr[k]
        k = (k+1)%len(arr)
    print(lin_arr)

linearization(arr, 4, 7)