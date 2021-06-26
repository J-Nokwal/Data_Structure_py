
def idk():
    if not sorted(queue)==queue:
        return True
    for i in queue:
        #if stack[0]<i: #
        if stack[-1]<=i:
            # queue.append(stack.pop())
 
            return True
    
    return False


n = int(input())
data = list(map(int, input().split()))
stack = [] # [] top
queue = [] # front [] rear
temp=[]
crr=1
print(data[0])
queue.append(data[0])
while crr<n:
    if data[crr]>=queue[-1]: # a
        #print("1111")
        queue.append(data[crr])
    elif len(stack)<=0 or data[crr]<=stack[-1]: # b
        #print("2222")
        stack.append(data[crr])
    else: # c
        # c i
        #print("333")
        while len(stack)>0:
            
            if (stack[-1]<queue[0]):
                print("111k")
                queue.append(stack.pop())
                continue
            elif(not idk()):
                print("222k")
                queue.append(stack.pop())
                print(queue)
                continue
            elif(stack[-1]==queue[-1]):
                print("3333k")
                queue.append(stack.pop())
                continue
            else:
                print("4444k")
                queue.append(queue[0])
                queue.remove(queue[0])
        # c ii
        while True:
            if queue[0]<data[crr]:
                queue.append(queue[0])
                queue.remove(queue[0])
            else:break
        # c iii
        stack.append(queue[0])
        queue.remove(queue[0])
        # c iv
        stack.append(data[crr])
        # c v
        while True:
            if queue[0]>=queue[-1]:
                queue.append(queue[0])
                queue.remove(queue[0])
            else:
                break
    # increment in outer loop
    crr+=1
    
    # print 
    if len(queue)>0 :
        for j in queue:
            print(j,end=" ")
        print()
    if len(stack)>0:
        for j in reversed(stack):
            print(j,end=" ")
        print() 

# 10
# 3 1 5 2 6 4 9 7 10 8

# 11 
# 3 1 5 2 6 4 9 7 10 8 0

# 