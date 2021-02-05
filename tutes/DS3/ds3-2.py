class node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class list_1():
    start=None

    def push(self,data):
        p=node(data,None)
        if self.start==None:
            p.next=p
        else :
            p.next=self.start
            q=self.start
            while(q):
                if q.next==self.start:
                    q.next=p
                    break
                q=q.next
        self.start=p
        

    def print_ls(self):
        q=self.start
        while(q):
            print(q.data,end='-->')
            q=q.next
            if q==self.start:
                print(q.data)
                break


ls=list_1()
ls.push(60)
ls.push(80)
ls.push(40)
ls.push(100)
ls.push(20)
ls.print_ls()