#in this lecture we will learned about the linear array
#we also learned how to insert, delete element in linear array


class Array():
    def __init__(self, src):
        array = self.create_arr(src)
        self.array = array
        
       

    def create_arr(self):
        length = len(self.array)
        
        arr = [None]*length
        for i in range(length):
            arr[i] = self.array[i]

        return arr

    def leftshift(self,src):
        
        for i in range(1, len(src)):
            src[i-1]=src[i]
        last_idx = -1
        src[last_idx] =None    
        
        self.src = src
        return src

    def rightshift(self, src):
        
        for i in range(len(src)-1, 0, -1):
            src[i]=src[i-1]
        
        src[0] =None    
        self.src = src
        return src

  

            


arr1 = [1,2,3,4,5,6]
array = Array(arr1)
new_arr = array.create_arr()

left1 = array.leftshift(new_arr)
print(left1)
left2 = array.leftshift(left1)
print(left2)

right1 = array.rightshift(new_arr)
print(right1)
