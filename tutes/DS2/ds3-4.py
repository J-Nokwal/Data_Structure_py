class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class list1():
    def __init__(self):
        self.start=None
    
    def insert_beginning(self,data):
        q=node(data,self.start)
        self.start=q
    
    def insert_end(self,data):
        q=self.start
        if q==None:
            self.insert_beginning(data)
            return
        while(q):
            if q.next==None:
                q.next=node(data)
                break
            else:q=q.next

    def reverse(self):
        prev = None
        q = self.start
        while(q != None):
            next = q.next
            q.next = prev
            prev = q
            q = next
        self.start = prev 

    
    def display(self):
            q=self.start
            while(q):
                print(q.data,end=" --> ")
                q=q.next
            print("Null")

obj=list1()
obj.insert_beginning(1)
obj.insert_end(2)
obj.insert_end(3)
obj.insert_end(4)
obj.insert_end(5)
obj.insert_end(6)
obj.insert_end(7)
obj.insert_end(8)
obj.reverse()
obj.display()