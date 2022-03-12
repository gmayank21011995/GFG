

class binary_search_tree:
    
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = binary_search_tree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = binary_search_tree(data)
    
    def search(self,data):
        if self.key == data:
            print("data found")
            return
        
        if self.key > data:
            if self.left:
                self.left.search(data)
            else:
                print("not found")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("not found")
    
    def pre_order(self):
        """root->left->right"""
        
        print(self.key,'-->',end='')
        
        if self.left:
            self.left.pre_order()
            
        if self.right:
            self.right.pre_order()
                    
    def in_order(self):
        """left->root->right"""
        
        #global prev
        
        if self.left:
            self.left.in_order()
        
        print(self.key,'-->',end='')
        
        
        if self.right:
            self.right.in_order()
        
        
    def post_order(self):
        """left->right->root"""
        
        if self.left:
            self.left.post_order()
        
        if self.right:
            self.right.post_order()
            
        print(self.key,'-->',end='')

obj = binary_search_tree(10)
obj.insert(15)
obj.insert(20)
obj.insert(5)
obj.insert(17)
obj.insert(13)

obj.in_order()
print()
obj.pre_order()
print()
obj.post_order()
print()
obj.search(20)
        