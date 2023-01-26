#in this lecture we learned about circular array
#how to use circular array

class Circular_Array:
    def __init__(self, src):
        cir_arr = self.crt_cir_array(src)        
        self.cir_arr = cir_arr

    def crt_cir_array(self, src):
        arr = [None]*len(src)
        for i in range(len(src)):
            arr[i]=src[i]
        return arr

    def left_rotate(self):
        temp = self.cir_arr[0]
        
        for i in range(1, len(self.cir_arr)):
            self.cir_arr[i-1] = self.cir_arr[i]
            
        self.cir_arr[len(self.cir_arr)-1] = temp
        print(self.cir_arr)
        

    def right_rotate(self):
        temp = self.cir_arr[-1]
        for i in range(len(self.cir_arr)-1, 0, -1):
            self.cir_arr[i]=self.cir_arr[i-1]
        self.cir_arr[0] = temp
        print(self.cir_arr)
        
        return self.cir_arr

    def __idx_increase(self):
        new_arr = [None]*(len(self.cir_arr)+1)
        for i in range(len(self.cir_arr)):
            new_arr[i] = self.cir_arr[i]
        self.cir_arr = new_arr
        
        return self.cir_arr

    def __idx_decrease(self):
        arr = [None]*(len(self.cir_arr)-1)
        for i in range(len(arr)):
          arr[i] = self.cir_arr[i]

        self.cir_arr = arr
        return self.cir_arr    

    def insert_into_index(self, index:int=None, value:int=None):
        if index==None and value==None:
          print("Please Insert at least Index or Index and Value")
          return
        arr = self.__idx_increase()
        
                
        for i in range(len(arr)-1, index, -1):
            arr[i]=arr[i-1]
        arr[index] = value

        self.cir_arr = arr
        return self.cir_arr
    def remove_from_index(self, index:int=None):
        self.cir_arr[index] = None
        
        for i in range(index+1, len(self.cir_arr)):
          
          self.cir_arr [i-1]=self.cir_arr[i]
          self.cir_arr[i] = None
        self.cir_arr = self.__idx_decrease()
          

        return self.cir_arr
      
   

arr = [1,2,3,4,5,6]
arr1 = Circular_Array(arr)
arr1.right_rotate()
arr1.right_rotate()
arr1.left_rotate()
print(arr1.insert_into_index(1))
print(arr1.remove_from_index(1))
