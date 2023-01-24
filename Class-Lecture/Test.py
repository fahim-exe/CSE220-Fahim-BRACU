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



arr = [1,2,3,4,5]
array1 = Array(arr)
array2 = Array(arr)
print(array1.leftshift())
print(array2.rightshift())
