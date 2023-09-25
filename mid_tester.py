def palindrome(circ, start, size):
    count = 0
    flag = False
    left = start
    last =(start+size-1)%len(circ)
    for i in range(size//2):
        if circ[left]==circ[last]:
            count = count + 1
            flag = True
        else:
            flag = False
            break

        left = (left+1)%len(circ)
        last = last - 1
        if last == -1:
            last = len(circ)-1

    if flag == True:
        return circ


def addArrays(arr1, arr2):
    if len(arr1)!=len(arr2):
        return f"Not the same lenght array"

    c2 = len(arr1)-1
    l = len(arr1)
    new_arr = [None]*l
    for i in range(l):
        a1 = arr1[i]
        if a1==None:
            a1 = 0
        a2 = arr2[c2]
        if a2==None:
            a2=0
        temp = int(a1)+int(a2)
        new_arr[i] = temp


        c2 = c2-1

    return new_arr

ar1 = [1,4,5,8,None,None,None]
ar2 = [7,4,8,9,5,None, None]

def has_cycle(arr):
    count = 0
    a = arr[count]

    while a!=None:
        count +=1
        a = arr[count]
    print(count)

arr = [1,2,3,4,5,6,None]

has_cycle(arr)

def count(head):
    count =0
    current = head
    while current!=None:
        print(current.value)
        current=current.next
        count+=1

    return count