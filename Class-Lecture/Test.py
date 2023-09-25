def copyList(self):
    copy_head = None
    copy_tail = None

    temp = self.head

    while temp!=None:
        n = Node(temp.elem, None)
        if copy_head==None:
            copy_head = n
            copy_tail = copy_head

        else:
            copy_tail.next = n
            copy_tail = copy_tail.next

        temp = temp.next
    return copy_head