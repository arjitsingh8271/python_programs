#Stack using Linked List
class Node:
    def __init__(self,dv=None):
        self.data=dv
        self.next=None
class Stack:
    def __init__(self,MS):
        self.MS=MS
        self.top=-1
        self.data=None
        self.next=None    
    def isEmpty(self):
        return(self.top==-1)
    def isFull(self):
        return(self.top==self.MS-1)
    def append(self,val1):
        if self.isFull():
            print("STACK IS FULL")
            return
        if self.isEmpty():
            self.data=val1
            self.top+=1
            return
        temp=self
        while temp.next!=None:
            temp=temp.next
        newNode=Node(val1)
        temp.next=newNode
        self.top+=1
    def delete_last_node(self):
        if self.isEmpty():
            print("STACK IS EMPTY")
            return
        if self.next==None:
            self.data=None
            self.top-=1
            return 
        temp=self
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        self.top-=1
    def __str__(self):
        datalist=""
        if self.isEmpty():
            print("EMPTY")
            return datalist
        else:
            if self.data is None:
                return datalist
            datalist+=str(self.data) + " "
            temp=self
            while temp.next!=None:
                temp=temp.next
                datalist+=str(temp.data) + " "
            return datalist

n=Stack(7)
n.append(10)
n.append(12)
n.append(13)
n.append(14)
n.append(16)
print(n)
n.delete_last_node()
n.delete_last_node()
n.delete_last_node()
n.delete_last_node()
n.delete_last_node()
n.delete_last_node()
#n.delete_last_node()
print(n)



    
