# def findCombination(n,cost,maxcost,minCost,s):
#     a=[1]*(n-1)
#     temp1=0
#     last=n-2
#     while True:
#         if sum(a)==cost:
#             break
#         if temp1==last:
#             temp1=0
#             last-=1
#         a[temp1]+=1
#         temp1+=1
#     return a


def findCombination(n):
    a=[1]*(n-1)
    temp1=0
    top=n
    while True:
        if sum(a)==cost:
            break
        if top==a[temp1]:
            temp1+=1
            top-=1
        a[temp1]+=1
    return a




t = int(input())
mlist=[]
for i in range(t):
    n = list(map(int, input().split()))
    mlist.append(n)
    print(n)
for i in range(t):
    s=list(range(1,mlist[i][0]+1))
    # print(s)
    cost=mlist[i][1]
    n=mlist[i][0]
    maxcost=sum(s)-1
    minCost=n-1
    if cost>maxcost or cost<minCost:
        print("Case #{}: IMPOSSIBLE".format(i+1))
        continue
    else:
        combination=findCombination(n)
        print(combination)
        cIndex=0
        Index=0
        last=n
        flag=True
        for i in range(n-1):
            # print(combination[i])
            if combination[cIndex]==1:
                cIndex+=1
                continue
            if flag==False:
                last=combination[cIndex]
            else:
                last=combination[cIndex]+1
            
            s[Index:last]=reversed(s[Index:last])
            print(s)
            cIndex+=1
            # last-=1
            if flag==False:
                flag=True
                Index+=1
            else:
                flag=False
        print((s))


# 2467531


# 1
# 7 27
# [7, 27]
# [7, 6, 5, 4, 3, 2]
# [7, 6, 5, 4, 3, 2, 1]
# [2, 3, 4, 5, 6, 7, 1]
# [2, 7, 6, 5, 4, 3, 1]
# [2, 5, 6, 7, 4, 3, 1]
# [2, 5, 7, 6, 4, 3, 1]
# [2, 5, 7, 6, 4, 3, 1]
# [2, 5, 7, 6, 4, 3, 1]