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
    #how about that
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


    def delete_node(self, key):   #method for deleting the nodes: case1 & case2

        # case1 : where we're to delete the head node of the list. 
        cur = self.head

        if cur and cur.data == key:   # key gives which node to delete
            self.head = cur.next      # setting node to next element in the list
            cur = None                # for getting rid of the removed head and making way for the next element to become head.
            return
        
        # case2 : where we have to delete a 'non-head' node in the linked list.
        previous = None                
        while cur and cur.data != key:   # procedure to find the element to be deleted
            previous = cur
            cur = cur.next

        if cur is None:                  # if element to be deleted is not in the list
            return

        previous.next = cur.next         # when element is found 
        cur = None                       # this removes the element  

    """
    def delete_at_position(self, pos):    # this method is for when there's a specific position in the list whose element needs to be deleted

        cur = self.head                  

        if pos == 0:                  # checking for the position to be head
            self.head = cur.next      
            cur = None
            return

        previous = None               # checking for any other position 
        count = 1                     # variable to keep track of the position in the loop
        while cur and count != pos:
            previous = cur
            cur = cur.next
            count += 1

        if cur is None:               # when position exceeds the available positions
            return

        previous.next = cur.next
        cur = None   
    """
    def length(self):
        
        count = 0
        cur = self.head

        while cur:
            count += 1
            cur = cur.next
        return count

    def length_recursive(self, node):

        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)
                    



llist = LinkedList()
llist.append("A")              
llist.append("B")
llist.append("C")
llist.append("D") # added elements using the append function only

##llist.insert_after(llist.head.next, "E") 
# llist.head.next is used here to point out the data element present just "next" to the head of the list.

# llist.prepend("E") # prepend example 

llist.delete_node("B")   # case2 when deletion of some element takes place which is not the head.

llist.print_list()
