def circular_array(arr):
    pass

def linearize_circular(arr, start:int=None):
    count = 0
    
    for i in range(len(arr)):
        if arr[i]!=None:
            count+=1

    linear_arr = [None]*count
    for i in range(len(linear_arr)):
        linear_arr[i]=arr[start]
        start=(start+1)%len(arr)
        
    print(linear_arr)


def left_rotate(arr, start):
    print(arr)
    temp = arr[0]
    temp2 = arr[start-1]
    for i in range(len(arr)):

        arr[start-1]=arr[start]
        start=(start+1)%len(arr)
    
    arr[len(arr)-1]=temp
    

    print(arr)



 
arr = [5,6,None,None,55,66,77]
#linearize_circular(arr, 4)

left_rotate(arr, 4)