# node
class node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        # self.history=next

# linked list class
class linked_list():
    def __init__(self):
        self.start=None

    def at_end(self,data):
        p=node(data)
        if self.start==None:
            self.start=p
            return
        else:q=self.start
        while(q):
            if q.next==None:
                q.next=p
                break
            q=q.next
    def insert_beg(self,data):
        q=node(data,self.start)
        self.start=q

    def insert(self,data,pos):
        # print(type(pos),pos)
        if pos.next==None:
            self.at_end(data)
            return
        p=node(data,pos.next)
        pos.next=p

    def search(self,data):
        q=self.start
        while(q):
            if q.data==data:
                return q 
            else: q=q.next
        return False

    # Returns data of previous node 
    def search2(self,data):
        q=self.start
        if q.data==data:
            return 0
        while(q.next):
            if q.next.data==data:
                return q 
            else: q=q.next
        return False

    def mid(self,data,start,end):
        q=self.start
        while(True):
            if q.data==start:
                break
            q=q.next
        a=q
        
        while(True):
            if q.data==end :
                val=a.data
                a=self.search2(val)
                break
            if q.next.data==end:  
                
                break
            if q.next.next!=None:
                a=a.next
                q=q.next.next
            else:
                break
        self.insert(data,a)

    # def iscircular(self):
    #     global circular_cheak
    #     q=self.start
    #     while(q):
    #         q=q.next
    #         if q==self.start:
    #             circular_cheak=True
    #             return True
        
    def pointer(self,point_data,count):
        global circular_cheak
        global final_list
        q=self.search(point_data)
        present=False
        a=q.next
        b=q
        #self.iscircular()
        if count==1:
            return
        
        for i in range(count):
            if q.next==None:
                q.next=self.start
                circular_cheak=True
            q=q.next

        for i in final_list:
            if a==i[1]:
                if i[2]==2:
                    final_list.remove([a.data,a,2])
                    break
                else: 
                    i[2]-=1
                    break
        b.next=q

        for i in final_list:
            if q==i[1]:
                i[2]+=1
                present=True
        
        if present==False:
            #print("appendind data:",q.data)
            final_list.append([q.data,q,2])

        #print(final_list)

    def cheakForTreeNode(self):
        global final_list
        k=False
        kl=[]
        for i in final_list:
            q=self.start
            for j in range(100):
                if q==None:
                    break
                if q==i[1]:
                    k=True
                else: q=q.next
            if k==False:
                #print("1111k",i)
                kl.append(i)     
        for i in kl:
            final_list.remove(i)     

    def printl(self):
        q=self.start
        while(q):
            print(q.data,end=" ")
            q=q.next
            if q==self.start:
                break
        print()

# input data
first_line= int(input())
cmd=[]
for i in range(first_line):
    cmd.append(list(input().split()))
 
circular_cheak=False
final_list=[]

ls=linked_list()

for info in cmd:
    if info[0]=='I':
        if int(info[1])==0:
            ls.at_end(int(info[2]))

        elif int(info[1])==1:
            a=ls.search(int(info[2]))
            if a!=False:
                ls.insert(int(info[3]),a)
                continue
            a=ls.search2(int(info[3]))
            if a==0:
                ls.insert_beg(int(info[2]))
            else:ls.insert(int(info[2]),a)

        elif int(info[1])==2:
            ls.mid(int(info[4]),int(info[2]),int(info[3]))
        continue
    
    if info[0]=='U':
        ls.pointer(int(info[1]),int(info[2]))

#ls.cheakForTreeNode()
final_list.sort()
#print(final_list)
mul_pointers=len(final_list)
#ls.iscircular()
if circular_cheak:
    print(1)
else:print(0)

if mul_pointers!=0: 
    print(len(final_list))
    for j in final_list:
        print(j[0],end=" ")
    print()
    for j in final_list:
        print(j[2],end=" ")
    print()
else:
    print(0)
    ls.printl()


# 6
# I 0 1
# I 0 7 
# I 1 6 7
# I 1 1 2
# I 2 1 7 3
# I 2 1 7 4

# 8
# I 0 1
# I 0 2
# I 0 3
# I 0 4
# I 0 5
# I 0 6
# I 0 7
# U 7 1


# 7
# I 0 1
# I 0 2
# I 0 3
# I 0 4
# I 0 5
# I 2 1 5 9
# I 1 12 1

# 8
# I 0 1
# I 0 2
# I 0 3
# I 0 4
# I 0 5
# I 0 6
# I 0 7
# U 1 15

# 8
# I 0 1
# I 0 2
# I 0 3
# I 0 4
# I 0 5
# I 0 6
# I 0 7
# U 1 7