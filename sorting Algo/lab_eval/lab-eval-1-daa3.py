from typing import final


m, n, pos = map(int, input().split())
dic = {}
for i in range(m*n):
    a = list(map(int, input().split()))
    dic[a[0]] = a[1:]

# dic = {
#     1: [0, 0, 1, 1, 1, 0, 0, 0],
#     2: [0, 0, 1, 0, 1, 1, 1, 0],
#     3: [0, 0, 1, 1, 0, 1, 1, 0],
#     4: [0, 0, 0, 0, 1, 1, 1, 0],
#     5: [0, 0, 1, 1, 1, 0, 0, 0],
#     6: [0, 0, 1, 1, 1, 1, 1, 0],
#     7: [0, 0, 1, 1, 0, 1, 1, 0],
#     8: [0, 0, 0, 0, 1, 0, 1, 0],
#     9: [1, 1, 1, 0, 1, 0, 0, 0],
#     10: [1, 1, 0, 0, 0, 1, 1, 1],
#     11: [0, 1, 1, 1, 0, 0, 0, 0],
#     12: [1, 0, 0, 0, 1, 1, 1, 1],
#     13: [1, 1, 0, 0, 1, 0, 0, 0],
#     14: [1, 1, 1, 1, 0, 0, 0, 1],
#     15: [0, 0, 0, 0, 1, 1, 1, 1],
#     16: [1, 0, 0, 0, 1, 0, 0, 1],
#     17: [1, 1, 0, 0, 1, 0, 0, 0],
#     18: [0, 0, 1, 1, 1, 0, 0, 0],
#     19: [0, 1, 1, 1, 0, 1, 1, 0],
#     20: [1, 0, 0, 0, 1, 0, 1, 1],
#     21: [1, 0, 0, 0, 1, 0, 0, 0],
#     22: [0, 1, 1, 0, 1, 0, 0, 0],
#     23: [1, 0, 0, 0, 0, 1, 1, 1],
#     24: [1, 0, 0, 0, 0, 0, 0, 0],
#     25: [1, 0, 0, 1, 1, 0, 0, 0],
#     26: [1, 1, 1, 1, 0, 0, 0, 0],
#     27: [0, 0, 0, 0, 1, 0, 1, 1],
#     28: [1, 0, 0, 1, 1, 0, 0, 1],
#     29: [1, 0, 0, 0, 1, 1, 0, 0],
#     30: [1, 1, 0, 1, 1, 0, 0, 0],
#     31: [0, 0, 1, 1, 1, 1, 0, 0],
#     32: [0, 0, 0, 0, 1, 1, 1, 0],
#     33: [1, 0, 1, 0, 0, 0, 0, 0],
#     34: [0, 0, 0, 0, 0, 0, 1, 1],
#     35: [1, 0, 0, 0, 0, 0, 0, 1],
#     36: [1, 1, 1, 0, 0, 0, 0, 0],
#     37: [1, 0, 0, 0, 0, 0, 1, 1],
#     38: [1, 1, 1, 0, 0, 0, 0, 0],
#     39: [1, 1, 1, 0, 0, 0, 1, 1],
#     40: [1, 0, 0, 0, 0, 0, 1, 1],
# }
# m,n,pos=5 ,8 ,20

visited=[pos]
queue=[[pos]]
final=[]
k=[1,n,n*m-n+1,n*m]
def fxn(x):
    global temp
    global final
    global queue
    global k
    if x in k:
        k.remove(x)
        final.append(a+[x])
        visited.append(a+[x])
        temp+=1
        return
        
    if x in visited:
        return
    queue.append(a+[x])
    visited.append(x)
    
    
    
temp=0
if pos in k:
    temp+=1
    final.append([pos])
    k.remove(pos)
while temp<4:
    a=queue.pop(0)
    aLast=a[-1]
    if dic[aLast][0]==1:
        fxn(aLast-n)
    if dic[aLast][1]==1:
        fxn(aLast-n+1)
    if dic[aLast][2]==1:
        fxn(aLast+1)
    if dic[aLast][3]==1:
        fxn(aLast+n+1)
    if dic[aLast][4]==1:
        fxn(aLast+n)
    if dic[aLast][5]==1:
        fxn(aLast+n-1)
    if dic[aLast][6]==1:
        fxn(aLast-1)
    if dic[aLast][7]==1:
        fxn(aLast-n-1)

# for j in final:
#     for i in j:
#         print(i,end=' ')
#     print()

final.sort(key=lambda x:x[-1])
for j in final:
    for i in j:
        print(i,end=' ')
    print()


# 2 2 1
# 1 0 0 1 1 1 0 0 0
# 2 0 0 0 0 1 1 1 0
# 3 1 0 0 0 0 0 1 1
# 4 1 1 1 0 0 0 0 0