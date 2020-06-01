class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    # to append element at the end of the Linked List    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  
    # to prepend the element i.e. in the beginning of the Linked List
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    # to insert the element after a given node
    def insert_after(self, prev, data):
        if not prev:
            print("Previous node not found")  
            return 
        new_node = Node(data)

        new_node.next = prev.next
        prev.next = new_node     

llist = LinkedList()
llist.append("A")              
llist.append("B")
llist.append("C")
llist.append("D") # added elements using the append function only

llist.insert_after(llist.head.next, "E") 
# llist.head.next is used here to point out the data element present just "next" to the head of the list.

# llist.prepend("E") # prepend example 

llist.print_list()
