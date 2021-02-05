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

    def count(self,count_val):
        q=self.start
        self.count=0
        if q.data==count_val:
            self.start=q.next
            self.count+=1
        while(q):
            if q.next.data==count_val:
                q.next=q.next.next
                self.count+=1
            q=q.next
        print(self.count)

    
    def display(self):
            q=self.start
            while(q):
                print(q.data,end=" --> ")
                q=q.next
            print("Null")

obj=list1()
obj.insert_beginning(1)
obj.insert_end(2)
obj.insert_end(1)
obj.insert_end(2)
obj.insert_end(1)
obj.insert_end(3)
obj.insert_end(1)
obj.count(1)
obj.display()