t = int(input())
mlist=[]
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    mlist.append([n,l])
# print("clear")
for m in range(t):
    n,l=mlist[m]
    sum=0
    for i in range(n-1):
        minItem=min(l[i:n])
        index=l.index(minItem)
        sum=sum+(index-minItem+2)
        j=l[index+1:i]
        l[i:index+1]=reversed(l[i:index+1])
        print(l,(index-minItem+2))
        # if m==2:
        #     print(l)
    # print("Case #"+str(m+1)+": "+sum)
    print("Case #{}: {}".format(m+1,sum))


# 6, 7, 5, 4, 3, 2, 1
# 4 5 3 6 2 7 1

# 3
# 4
# 4 2 1 3
# 2
# 1 2
# 7
# 7 6 5 4 3 2 1

# 2765431
# 1345672
# 1276543

# 2 4 6 7 5 3 1
# 1357642
# 1246753
# 1235764
# 1234675
# 1234576
# 1234567

# 12467531