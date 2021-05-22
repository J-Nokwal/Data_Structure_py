# # def findCost(x,y,s):
# #     return (x*s.count('CJ'))+(y*s.count('JC'))
# positive_infnity = float('inf')
# def fxn(x,y,s,mincost,k):
#     for i in k:
#         if '?'*i in s:
#             mincost=fxn(x,y,s.replace('?'*i,'C'*i,1),mincost,k)
#             mincost=fxn(x,y,s.replace('?'*i,'J'*i,1),mincost,k)
#             return mincost
#     # if '???' in s:
#     #     mincost=fxn(x,y,s.replace('???','CCC',1),mincost)
#     #     mincost=fxn(x,y,s.replace('???','JJJ',1),mincost)
#     # elif '??' in s:
#     #     mincost=fxn(x,y,s.replace('??','CC',1),mincost)
#     #     mincost=fxn(x,y,s.replace('??','JJ',1),mincost)
#     # elif '?' in s:
#     #     mincost=fxn(x,y,s.replace('?','C',1),mincost)
#     #     mincost=fxn(x,y,s.replace('?','J',1),mincost)
#     #     return mincost
#     cost=(x*s.count('CJ'))+(y*s.count('JC'))
#     if mincost > cost or mincost==-1:
#         mincost=cost
#     return mincost
    


# t = int(input())
# mlist=[]

# for i in range(t):
#     x,y,s = input().split()
#     mlist.append([int(x),int(y),s])
# # print(mlist)
# # print('clear')
# for m in range(len(mlist)):
#     x,y,s=mlist[m]
#     k=[]
#     for i in range(len(s)-1,0,-1):
#         if '?'*i in s:
#             k.append(i)
#     print("Case #{}: {}".format(m+1,fxn(x,y,s,positive_infnity,k)))
    
    





# # ???j??j??c?c??c?j?c
# # cjjc
















# positive_infnity = float('inf')
# def fxn(x,y,s,mincost):
#     print(s)
#     if '?' in s:
#         if 'C?C' in s:
#             if x<y:
#                 mincost=fxn(x,y,s.replace('?','C',1),mincost)
#             return mincost
#         elif 'J?J' in s:
#             mincost=fxn(x,y,s.replace('?','J',1),mincost)
#             return mincost
#         # elif 'C??' in s or 'C?J' in s:
#         elif 'C?J' in s:
#             if x<y:
#                 mincost=fxn(x,y,s.replace('?','C',1),mincost)
#             else:
#                 mincost=fxn(x,y,s.replace('?','J',1),mincost)
#             return mincost
#         # elif 'J??' in s or 'J?C' in s:
#         elif 'J?C' in s:
#             if x>y:
#                 mincost=fxn(x,y,s.replace('?','C',1),mincost)
#             else:
#                 mincost=fxn(x,y,s.replace('?','J',1),mincost)
#             return mincost
#         # '?' at end
#         else:
#             mincost=fxn(x,y,s.replace('?','C',1),mincost)
#             mincost=fxn(x,y,s.replace('?','J',1),mincost)
#             return mincost



#     cost=(x*s.count('CJ'))+(y*s.count('JC'))
#     if mincost > cost or mincost==-1:
#         mincost=cost
#     return mincost
    


# t = int(input())
# mlist=[]

# for i in range(t):
#     x,y,s = input().split()
#     mlist.append([int(x),int(y),s])
# for m in range(len(mlist)):
#     x,y,s=mlist[m]
#     # if s[0:2]=='?C':
#     #     print("Case #{}: {}".format(m+1,fxn(x,y,s.replace('?','C',1),positive_infnity)))
#     # elif s[0:2]=='?J':
#     #     print("Case #{}: {}".format(m+1,fxn(x,y,s.replace('?','J',1),positive_infnity)))
#     if s[0]=='?':
#         a=fxn(x,y,s.replace('?','C',1),positive_infnity)
#         b=fxn(x,y,s.replace('?','J',1),positive_infnity)
#         print("Case #{}: {}".format(m+1,min(a, b)))
#     else:
#         print("Case #{}: {}".format(m+1,fxn(x,y,s,positive_infnity)))
    
















def findCost(x,y,s):
    return (x*s.count('CJ'))+(y*s.count('JC'))

def fxn(x,y,s,mincost):
    # print(s)
    if '?' in s:
        a=findCost(x,y,s.replace('?','C',1))
        b=findCost(x,y,s.replace('?','J',1))
        if a==b:
            mincost=fxn(x,y,s.replace('?','C',1),mincost)
            mincost=fxn(x,y,s.replace('?','J',1),mincost)
        elif a<b:
            mincost=fxn(x,y,s.replace('?','C',1),mincost)
        else: 
            mincost=fxn(x,y,s.replace('?','J',1),mincost)
        return mincost
    cost=findCost(x,y,s)
    if mincost > cost or mincost==-1:
        mincost=cost
    return mincost
    


t = int(input())
mlist=[]

for i in range(t):
    x,y,s = input().split()
    mlist.append([int(x),int(y),s])
# print(mlist)
# print('clear')
for m in range(len(mlist)):
    x,y,s=mlist[m]
    print("Case #{}: {}".format(m+1,fxn(x,y,s,-1)))
    
    