# manual and simple way

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

'''node1 = Node("3")
node2 = Node("7")
node3 = Node("10")
node4 = Node("77")

node1.next = node2
node2.next = node3
node3.next = node4

current_node = node1
while True:
    print(current_node.value, "-> ", end="")
    if current_node.next is None:
        print("None")
        break
    current_node = current_node.next'''


class linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = node
                break
            current_node = current_node.next



    def print_link_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, "-> ", end="")
            current_node = current_node.next
        print("None")



ll = linked_list()

ll.insert("3")

ll.insert("44")

ll.insert("55")
ll.print_link_list()
        