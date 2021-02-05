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

    def checkPalindrome(self):
        if self.start==None:
            return True
        left=self.start
        right=self.start
        while(right.next!=None):
            right=right.next
        #print(right.data)
        while(True):
            if left.data != right.data:
                return False
            left=left.next
            if left==right:
                return True
            right=right.prev
            if left==right:
                return True
        return False




    def print_list(self):
        q=self.start
        while(q):
            print("q:",q,"q.prev: ",q.prev,"q.data: ",q.data,"q.next",q.next)
            q=q.next

List=list1()
List.push('l')
List.push('e')
List.push('v')
List.push('v')
List.push('e')
List.push('l')
if List.checkPalindrome():
    print(True)
else: print(False)

#List.print_list()