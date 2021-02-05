class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class list1:
    def __init__(self):
        self.start=None

    def pushOnTop(self,data):
        p=node(data,None)
        if self.start==None:
            self.start=p
            return
        else:
            p.next=self.start
            self.start=p

    def pop(self):
        self.start=self.start.next

    def peek(self,newData):
        if self.start==None:
            print("Stack is Empty")
            return False
        if self.start.data==newData:
            self.pop()
            return True
        else:
            return False

    def display(self):
        q=self.start
        while(q):
            print(q.data,end=" ")
            q=q.next
        #print("Left side is Top")

newStack=list1()

for i in input("Enter Data: "):
    if i=='{' or i=='[' or i=='(':
        newStack.pushOnTop(i)
    elif i=='}':
        if not newStack.peek('{'):
            print('parantheses not correct expected: {')
            break
    elif i==']':
        if not newStack.peek('['):
            print('parantheses not correct expected: [')
            break
    elif i==')':
        if not newStack.peek('('):
            print('parantheses not correct expected: (')
            break