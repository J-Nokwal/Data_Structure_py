from queue import Queue

# def end(path):
#     if path=="":
#         i=1
#     j=0
    
#     pass

def valid(path):
    global size
    global data
    global que
    global end
    i=0
    j=0
    for k in range(len(path)):
        #print("kkkk",k)
        if path[k]=="1":
            #print("111k",path)
            i-=1
        elif path[k]=="2":
            #print("222k")
            j+=1
        elif path[k]=="3":
            #print("333k")
            i+=1
        elif path[k]=="4":
            #print("444k")
            j-=1
    if not (0<=i<size[0] and 0<=j<size[1]):
        #print("0<=i<size[0]",0,i,size[0],"\n0<=j<size[1]",0,j,size[1])
        return
    p = (i+1) + (j*size[1])
    m=data[p-1]
    print("final",p)

    if m[0]==size[0]*size[1]:
        end = True
        return

    for i in [1,2,3,4]:
        if m[i]==1:# and not (path[-1]==[1,2,3,4][i+1]):
            #print("iiiik",m,i)
            que.put(path+str(i))
        
    


size = list(map(int, input().rstrip().split()))
data=[]
for i in range(size[0]*size[1]):
    data.append(list(map(int, input().rstrip().split())))

# for i in data:
#     print(i)


que = Queue()
que.put("")
path=""
end =False
while not end:
    path=que.get()
    # print("kkk")
    # for i in ["1","2","3","4"]:
    #     new=path+i
    #     if valid(new):
    #         que.put(new)
    #print("going to run 1 more time",path)
    valid(path)
    # print("run 1 more time",path)
