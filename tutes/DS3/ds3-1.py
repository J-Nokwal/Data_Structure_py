class node:
    def __init__(self,data=None,prev=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class list_1:
    def __init__(self):  
        self.start = None

    def insert_beginning(self, data):
        p = node(data,None,self.start)
        self.start=p
        if p.next!=None:
            p.next.prev=p
    
    def insert_end(self,data):
        q=self.start
        if q==None:
            self.insert_beginning(data)
        while(q):
            if q.next==None:
                q.next=node(data,q,None)
                break
            if q.next==self.start:
                break
            q=q.next

    
    def insert_after(self,data,val):
        q=self.start
        if q==None:
            print("List is empty")
        while(q):
            if q.data==val:
                temp=q.next
                q.next=node(data,q,temp)
                temp.prev=q.next
                break
            if q.next==self.start:
                break
            q=q.next

    def insert_before(self,new_data,val):
        q=self.start
        if q==None:
            print("List is empty")
        while(q):
            if q.data==val:
                temp=q.prev
                q.prev=node(new_data,temp,q)
                temp.next=q.prev
                break
            if q.next==self.start:
                break
            q=q.next
    
    def deletion(self,val):
        q=self.start
        if q==None:
            print("List is empty")
        while(q):
            if q.data==val:
                if q.next==None:
                    q.prev.next=None
                    break
                if q.prev==None:
                    q.next.prev=None
                    break
                q.prev.next=q.next
                q.next.prev=q.prev
                break
            if q.next==self.start:
                break
            q=q.next

    def search(self,val):
        q=self.start
        if q==None:
            print("List is empty")
        while(q):
            if q.data==val:
                print(val," is prsent at node ",q)
                break
            if q.next==self.start:
                print(val," not found")
                break
            q=q.next

    def connect(self):
        q=self.start
        while(q):
            if q.next==None:
                q.next=self.start
                self.start.prev=q
                break
            q=q.next

    def print_list(self):
        q=self.start
        while(q):
            print("q:",q,"q.prev: ",q.prev,"q.data: ",q.data,"q.next",q.next)
            q=q.next
            if q==self.start:
                break

ls=list_1()
ls.insert_beginning(45)
ls.insert_beginning(11)
ls.insert_end(999)
ls.insert_before(123445,999)
ls.connect()
ls.deletion(45)
ls.insert_after(9898,999)
ls.insert_before(888,11)
ls.search(999)
ls.print_list()