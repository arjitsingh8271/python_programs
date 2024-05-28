class Node:
    def __init__(self, dv=None):
        self.data = dv
        self.next = None

    def isEmpty(self):
        return self.data is None

    def append(self, val1):
        if self.isEmpty():
            self.data = val1
            return
        temp = self
        while temp.next is not None:
            temp = temp.next
        newNode = Node(val1)
        temp.next = newNode

    def delete_first_node(self):
        if self.data is None:
            return
        if self.next is None:
            a=self.data
            self.data = None
            return a
        if self.next.next is None:
            a=self.data
            self.data = self.next.data
            self.next = None
            return a
        a=self.data
        self.data = self.next.data
        self.next = self.next.next
        return a

    def __str__(self):
        datalist = ""
        if self.data is None:
            return datalist
        datalist += str(self.data) + " "
        temp = self
        while temp.next is not None:
            temp = temp.next
            datalist += str(temp.data) + " "
        return datalist

    def __len__(self):
        if self.isEmpty():
            return 0
        c = 0
        temp = self
        while temp is not None:
            c = c + 1
            temp = temp.next
        return c


class Queue:
    def __init__(self,MS):
        self.n=Node()
        self.MS=MS

    def isEmpty(self):          
        return self.n.isEmpty()

    def isFull(self):
        return len(self.n)==self.MS

    def enqueue(self,ele):
        if not self.isFull():
            self.n.append(ele)
        else:
            print("Queue is Full")

    def dequeue(self):          
        if self.isEmpty():
            return("Queue is Empty")
        return self.n.delete_first_node()

    def __len__(self):     
        return len(self.n)

    def __str__(self):
        if not self.isEmpty():
            return str(self.n)
        else:
            return("Queue is Empty")
    

q = Queue(5)

q.enqueue(11)

q.enqueue(22)

q.enqueue(33)

q.enqueue(44)

q.enqueue(55)

q.enqueue(66)

print(q)

print("the length is",len(q))

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())

print("Dequeuing: ",q.dequeue())
