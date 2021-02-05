class node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class list1:
    def __init__(self):  
        self.start = None
  
    def insert_beginning(self, data):
        p = node(data,self.start)
        self.start=p

    def insert_end(self,data):
        q=self.start
        while(q):
            if q.next==None:
                q.next=node(data)
                break
            else:q=q.next
    
    def insert_after(self,data,after_val):
        q=self.start
        while(q):
            if q.data==after_val:
                temp=q.next
                q.next=node(data,temp)
                break
            else:
                q=q.next

    def deletion_beginning(self):
        if not self.start: 
            return None
        self.start=self.start.next
    
    def deletion_end(self):
        q=self.start
        while(q):
            if q.next.next==None:
                q.next=None
                break
            else:q=q.next

    def deletion_node(self,del_data):
        q=self.start
        temp=q
        while(q):
            if q.data==del_data:
                if q==self.start:
                    self.deletion_beginning()
                    break
                temp.next=q.next
                break
            else:
                temp=q
                q=q.next

    def search(self,search_val):
        q=self.start
        while(q):
            if q.data==search_val:
                print("Node is:",q,"\nNext node is: ",q.next)
                break
            else:q=q.next

    def display(self):
        q= self.start
        while(q):
            print(q.data,end=" ")
            q = q.next
        print()


obj= list1()
obj.insert_beginning(3)
obj.insert_beginning(6)
obj.insert_beginning(5)
obj.insert_end(312)
obj.insert_end(12)
obj.insert_end(34)
obj.insert_after(5656,3)
obj.deletion_beginning()
obj.deletion_node(6)
obj.deletion_end()
obj.search(12)
obj.display()
# ~5 ~6 3 5656 312 12 ~34