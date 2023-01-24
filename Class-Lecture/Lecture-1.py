#in this lecture we learned shifts (leftshift, rightshift)


class Array():
    def __init__(self, src):
        self.array = src
        
       

    def create_arr(self):
        length = len(self.array)
        
        arr = [None]*length
        for i in range(length):
            arr[i] = self.array[i]

        return arr

arr1 = [1,2,3,4,5,6]
array = Array(arr1)
print(array.create_arr())