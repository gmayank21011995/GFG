class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        n = self.head

        while n is not None:
            print(n.data,"-->",end="")
            n = n.ref
    
    def add_begin(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node
    
    def add_end(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            
            n.ref = new_node
    
    def add_after(self, data, x):
        if self.head is None:
            print("linked list is empty there is no ",x,"element.")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            
            if n is None:
                print(x, "not found in linked list")
                return
            
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def add_before(self, data, x):
        if self.head is None:
            print("linked list is empty, can't insert before ",x)
            return
        if self.head.data == x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print(x, "element not found")
            
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

obj = linkedlist()

obj.add_begin(10)
obj.add_begin(20)
obj.add_begin(40)
obj.traversal()
obj.add_end(100)
obj.add_end(10)
print()
obj.traversal()
obj.add_after(13,20)
obj.add_after(17,40)
print()
obj.traversal()
obj.add_before(23,100)
obj.add_before(39,10)
print()
obj.traversal()