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

    def mid(self):
        q=self.start
        count=0
        while(q):
            count+=1
            q=q.next
        
        q=self.start
        for x in range(count//2):
            q=q.next
        print("Mid value is:",q.data)
        # if count%2==1:
        #     q=self.start
        #     for x in range(count//2):
        #         q=q.next
        #     print(q.data)
        # elif count%2==0:
        #     q=self.start
        #     for x in range(count//2):
        #         q=q.next
        #     print(q.data)
    
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
obj.insert_end(33342234)
obj.insert_end(55555)
obj.insert_end(6)
obj.insert_end(7)
obj.insert_end(8)
obj.mid()
#obj.display()