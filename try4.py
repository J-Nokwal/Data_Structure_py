from queue import Queue

m,n = map(int, input().rstrip().split())
data={}
for i in range(m*n):
    a,b,c,d,e= map(int, input().rstrip().split())
    data[a]=[b,c,d,e]

for i in range(n):
    data[i+1][0]=0
    data[(m*n)-i][2]=0
for i in range(m):
    data[1+n*i][3]=0
    data[n*(i+1)][1]=0

def valid(a,dir):
    global data
    temp=a[:]

    if data[temp[-1]][dir-1]==0:
        return False

    if dir==1:
        next=a[-1]-n
    elif dir==2:
        next=a[-1]+1
    elif dir==3:
        next=a[-1]+n
    elif dir==4:
        next=a[-1]-1

    if next in temp:
        return False
    
    temp.append(next)
    que.put(temp)
    return True

def nextpath(crr,dir):
    pass

que = Queue()
que.put([1])
path=[]
notEnd = True
while notEnd:
    path=que.get()
    for i in [1,2,3,4]:
        if valid(path,i):
            pass
            # que.put(nextpath(path,i))
    if path[-1]==m*n:
        for i in path:
            print(i,end=" ")
        break
















# 5 8
# 1 0 1 1 0
# 2 0 1 1 1
# 3 0 1 0 1
# 4 0 0 1 1
# 5 0 1 1 0
# 6 0 1 1 1
# 7 0 1 0 1
# 8 0 0 1 1
# 9 1 1 1 0
# 10 1 0 0 1
# 11 0 1 0 0
# 12 1 0 1 1
# 13 1 0 1 0
# 14 1 1 0 0
# 15 0 0 1 1
# 16 1 0 1 0
# 17 1 0 1 0
# 18 0 1 1 0
# 19 0 1 0 1
# 20 1 0 1 1
# 21 1 0 1 0
# 22 0 1 1 0
# 23 1 0 0 1
# 24 1 0 0 0
# 25 1 0 1 0
# 26 1 1 0 0
# 27 0 0 1 1
# 28 1 0 1 0
# 29 1 0 1 0
# 30 1 0 1 0
# 31 0 1 1 0
# 32 0 0 1 1
# 33 1 1 0 0
# 34 0 0 0 1
# 35 1 0 0 0
# 36 1 1 0 0
# 37 1 0 0 1
# 38 1 1 0 0
# 39 0 1 0 1
# 40 1 0 0 1
