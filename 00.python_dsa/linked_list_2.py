class Node:
    
    def __init__(self,val=None):
        self.data=val
        self.next=None
    
    def isEmpty(self):
        return (self.data==None and self.next==None)
    
    def append(self,value):
        if self.isEmpty():
            self.data=value
            return
        temp=self
        while temp.next!=None:
            temp=temp.next
        newnode=Node(value)
        temp.next=newnode
        
    def insert_at_begin(self,value):
        if self.isEmpty():
            self.data=value
            return
        newnode=Node(value)
        self.data,newnode.data=newnode.data,self.data
        newnode.next=self.next
        self.next=newnode
    
    def insert_after_node(self,value,v):
        if self.isEmpty():
            return("insertion is not possible")
        newnode=Node(v)
        temp=self
        while temp.data!=value:
            if temp.next==None:
                return("The node is not present")
            else:
                temp=temp.next
        if temp.next!=None:
            newnode.next=temp.next
            temp.next=newnode
        else:
            temp.next=newnode
        
    def insert_before_node(self,value,v):
        if self.isEmpty():
            return("insertion is not possible")
        newnode=Node(v)
        temp=self
        if self.data==value:
            self.data,newnode.data=newnode.data,self.data
            newnode.next=self.next
            self.next=newnode
            return
        while temp.next.data!=value:
            if temp.next.next==None:
                return("The node is not present")
            else:
                temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    
    def insert_at_position(self,value,pos):
        if pos<0:
            return("invalid position")
        if self.isEmpty():
            return("the list is empty")
        if pos==0:
            self.insert_at_begin(value)
            return
        c=1
        temp=self
        while c!=pos:
            if temp.next==None:
                return("list is not present upto this position")
            else:
                temp=temp.next
                c=c+1
        newnode=Node(value)
        if temp.next!=None:
            newnode.next=temp.next
            temp.next=newnode
        else:
            temp.next=newnode
               
    def __str__(self):
        data=""
        temp=self
        if self.isEmpty():
            return("empty list")
        while temp.next!=None:
            data+=str(temp.data) + ""
            temp=temp.next
        data=data+str(temp.data) + ""
        return data
    
    def __len__(self):
        if self.isEmpty():
            return("the list is empty")
        c=0
        temp=self
        while temp.next!=None:
            temp=temp.next
            c=c+1
        c=c+1
        return(c)
            
    
print("list value")       
ll=Node(10)
print(ll)
ll.append(20)
print(ll)
ll.append(30)
print(ll)
ll.append(40)
print(ll)
print("length of the list is:",len(ll))
print("insertion at the begning of the node")
ll.insert_at_begin(5)
print(ll)
print("length of the list is:",len(ll))
print("insertion after a node")
ll.insert_after_node(20,25)
print(ll)
print("insertion before a node")
ll.insert_before_node(40,35)
print(ll)
print("insert at position given by user")
ll.insert_at_position(39,4)
print(ll)
print("length of the list is:",len(ll))