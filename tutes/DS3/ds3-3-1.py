class node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=print
        self.next=next

class list1():
    def __init__(self):
        self.start=None

    def push(self,data):
        p=node(data,None,self.start)
        if self.start!=None:
            self.start.prev=p
        self.start=p

    def count(self):
        q=self.start
        count=0
        while(q):
            count+=1
            q=q.next
        print("count:",count)


    def print_list(self):
        q=self.start
        while(q):
            print("q:",q,"q.prev: ",q.prev,"q.data: ",q.data,"q.next",q.next)
            q=q.next

List=list1()

print("111111k\n")
List.count()
List.push(777)
List.push(555)
List.push(3333)
List.push(235)
List.push(353)
List.push(335)
List.print_list()
List.count()