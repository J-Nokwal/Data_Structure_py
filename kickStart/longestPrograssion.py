from collections import defaultdict
def cost(l,s):
    dict=defaultdict(int)
    for i in range(1,l):
        a=s[i]-s[i-1]
        dict[a]+=1
    a=[]
    b=[]
    for i in dict.keys():
       a.append(i)
       b.append(dict[i]) 
    c=max(b)
    a=a[b.index(c)]
    return a,c


def change(l,s):
    dinit,init=cost(l,s)
    for i in range(2,l):
        a=s[i]-s[i-1]
        if a != dinit:
            temp=s[:]
            temp[i]=temp[i-1]+a
            d,p=cost(l, temp)
            if p>init:
                return init+1
    return init+1

        
    # for i in range(2,l):
    #     b=s[i]-s[i-1]
    #     if b!=a:
    #         temp=s[:]
    #         temp[i]=temp[i-1]+a
    #         p=cost(l, temp)
    #         if p>init:
    #             init=p
    #             return init+1
    #         a=b
    # return init+1
        # else:
            # pass



n=int(input())
arr=[]
for i in range(n):
    l=int(input())
    s=list(map(int, input().split()))
    arr.append([l,s])

for i in range(len(arr)):
    a=change(arr[i][0], arr[i][1])
    print('Case #{}: {}'.format(i+1,a))

# q=change(4,[8 ,5 ,2 ,0])
# print(q)