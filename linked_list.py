"""
Pure Python Implementation of Linked-list

"""

class node():
    def __init__(self, data):
        self.data = data
        self.next = None
     
    # In python getters and setters aren't really needed but are included as good practice. 
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next

     
class singly_linked_list():
    def __init__(self, head=None):
        self.head = head
        
    def traverse(self):
        curr = self.head
        print(curr.data)
        
        while curr.next != None:
            curr = curr.next
            print(curr.data)
            
    
    def get_size(self):
        curr = self.head
        counter = 1
        while curr.next != None:
            counter += 1
            curr = curr.next
        return counter
        
    def search_data(self, item):    
        curr = self.head   
        while curr:
            if curr.data == item:
                return True
            curr = curr.next
        
        raise ValueError("Data not Found...") 

    def get_list(self):
        mylist = []
        curr = self.head
        while curr:
            mylist.append(curr.data)
            curr = curr.next
        return mylist
    
    def insert_node(self, data):
        new = node(data)
        new.next = self.head
        self.head = new
    
if __name__ == '__main__':
    
    # Defining nodes
    node1 = node(100)
    node2 = node(200)
    node3 = node('1 million')
 
    node1.next = node2
    node2.next = node3
    
    
    # Defining Singly linked list
    sll = singly_linked_list(node1)
    sll.traverse()    
    sll.insert_node(800)
    
    print("Size of the Linked list: {}".format(sll.get_size()))
    
    if sll.search_data(200):
        print("Found Value")
        
    print(sll.get_list())
    
    
    
    
        