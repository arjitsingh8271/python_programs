class c_queue:

    def __init__(self, MS):
        self.arr = [None]*MS
        self.MS = MS
        self.front = self.rear = -self.MS-1

    def isFull(self):
        return (self.rear+1)%self.MS==self.front

    def isEmpty(self):
        return (self.front==-self.MS-1)

    def enqueue(self, ele):
        if self.isEmpty():
            self.front = self.rear = 0
            self.arr[self.rear] = ele
            return
        if self.isFull():
            print("C_QUEUE is Overflow")
            return
        self.rear = (self.rear+1) % self.MS
        self.arr[self.rear] = ele

    def dequeue(self):
        if self.isEmpty():
             print("C_QUEUE is Underflow")
        if (self.rear == self.front):
            ele = self.arr[self.front]
            self.front = self.rear = -self.MS-1
        else:
            ele = self.arr[self.front]
            self.front = (self.front+1)%self.MS
        return ele

    def __str__(self):
        data = ""
        if (self.front <= self.rear):
            for i in range (self.front, self.rear+1):
                data += str(self.arr[i] + " ")
        else:
            for i in range (self.front, self.MS):
                data += str(self.arr[i] + " ")
            for i in range (self.rear+1):
                data += str(self.arr[i] + " ")
        return (data)

    def __len__ (self):
        if (self.front <= self.rear):
            return (self.rear - self.front+1)
        else:
            return ((self.MS - self.front) + (self.rear+1))


cq = c_queue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)


cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()

"""
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
"""   
        
