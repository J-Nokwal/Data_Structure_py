import random
k=0
l=[]
count=0
while k<10:
    t=random.randint(0,1)
    if l!=[]:
        if l[0]==t:
            k+=1
            l.insert(t,0)
        else:
            k=0
            l=[]
    else:
        l.insert(t,0)
    count+=1
print(count)