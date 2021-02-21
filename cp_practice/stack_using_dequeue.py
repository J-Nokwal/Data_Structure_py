#https://www.geeksforgeeks.org/implement-stack-queue-using-deque/

class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Dequeue:
    def __init__(self):
        self.head=None
        self.tail-None
    def size(self):
        size=0
        p=self.head
        while p:
            size+=1
            p=p.next
        return size
    def isEmpty(self):
        if self.head==None:
            return True
        return False
    def isFull(self,n):
        temp=0
        p=self.next
        while(p):
            temp+=1
            p=p.next
        if temp>=n:
            return True
        return False

# not complete check for valid head    
    def inserFirst(self,data):
        head=self.head
        p=node(data)
        head.prev=p
        p.next=head
        head=p

# not complete check for valid head 
    def inserlast(self,data):
        head=self.head
        p=node(data)
        while head.next:
            head=head.next
        head.next=p
        p.prev=head
    
        