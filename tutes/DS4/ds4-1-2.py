class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class list1:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.start=None
        self.size=0

    def pushOnTop(self,data):
        p=node(data,None)
        if self.size >= self.maxSize:
            print("Stack Overflow")
        else:
            if self.start==None:
                self.start=p
                self.size+=1
                return
            else:
                p.next=self.start
                self.start=p
                self.size+=1

    def pop(self):
        if self.start==None:
            print("Stack is Empty")
            return
        self.start=self.start.next
    
    def isEmpty(self):
        if self.start==None:
            print("Stack is empty")
        else: print("Stack is not empty")
    
    def isFull(self):
        if self.size >= self.maxSize:
            print("stack is Full")
        else: print("Stack is not Full")

    def peek(self):
        if self.start==None:
            print("Stack is Empty")
        else:print(self.start.data)

    def display(self):
        q=self.start
        while(q):
            print(q.data,end=" ")
            q=q.next
        print("Left side is Top")

newstack = list1(int(input("Enter max Size of Stack: ")))
#newstack = Stack(3)
print(("----------------------\n1. Push\n2. pop\n3. isEmpty?\n4. isFull?\n5. Peek\n6. Display\n7. End operations\n"))
while (True):
    #k = int(input("----------------------\n1. Push\n2. pop\n3. isEmpty?\n4. isFull?\n5. Peek\n6. Display\n7. End operations\n"))
    k=int(input())
    if k == 1:
        # print("kkk-1")
        m = int(input("Enter Data to push: "))
        newstack.pushOnTop(m)
    elif k == 2:
        newstack.pop()
    elif k == 3:
        newstack.isEmpty()
    elif k == 4:
        newstack.isFull()
    elif k == 5:
        newstack.peek()
    elif k == 6:
        newstack.display()
    elif k == 7 :
        break