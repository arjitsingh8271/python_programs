class Node:
    def __init__(self,key=None):
        self.left=None
        self.data=key
        self.right=None
        
    def insert(self,key):
        if self.data==None:
            self.data=key
            return
        if self.data==key:
            return
        if key<self.data:
            if self.left==None:
                self.left=Node(key)
            else:
                self.left.insert(key)
        elif key>self.data:
            if self.right==None:
                self.right=Node(key)
            else:
                self.right.insert(key)
                
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end="  ")
        if self.right:
            self.right.inorder()
        
          
    def preorder(self):
        print(self.data,end="  ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end="  ")
        
          

    def search(self,key):
        if self.data==key:
            print(key,"Found")
            return True
        if self.data!=key and self.left==None and self.right==None:
            print(key,"Not Found")
            return False
        if key < self.data:
            self.left.search(key)
        else:
            self.right.search(key)

      
        

bst=Node()
bst.insert(20)
bst.insert(15)
bst.insert(40)
bst.insert(18)
bst.insert(60)
bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
print()
bst.search(18)
        
