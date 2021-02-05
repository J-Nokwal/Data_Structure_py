class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class list1:
    start=None
    def push(self,data):
        p=node(data,)
        if self.start==None:
            self.start=p
            return
        else:
            p.next=self.start
            self.start=p

    def display(self):
        q=self.start
        while(q):
            print(q.data,end="")
            q=q.next
        print()

newStack=list1()
for i in input("Enter String: "):
    if i==' ':
        continue
    newStack.push(i)
newStack.display()