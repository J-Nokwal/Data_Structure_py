from collections import OrderedDict
d,i,s,v,f= map(int, input().split())
#duration, intersection(nodes),streets,cars,bonus points
paths= []
nodeQueues=[[]for i in range(i)]
# scedule=[node_name,[street_name,duration_time_green]]#
class Scedule:
    streetData=[]
    def __init__(self,nodeName,):
        self.nodeName=nodeName
outputNodes=[]
paths=OrderedDict()

for _ in range(s):
    l= input().split()
    # paths.append([int(l[0]), int(l[1]), l[2], int(l[3])])
    paths[l[2]]=[int(l[1]),int(l[3])] #Street end

cars= []
for _ in range(v):
   l= input().split()
   cars.append([int(l[0]), l[1:],0])

#Main code


for duration in range(d):
    arr=[]
    for i in cars:
        arr.append(i[1].pop(0))
        nodeQueues[paths[i[1][0]][1]].append([i[0],i[1].pop()])
        i[2]+=1

    for i in nodeQueues:
        if len(i)>0:
            a,b=i.pop(0)
            node=Scedule(a)
            node.streetData.append([b,1])
    



#OUTPUT Data
print(len(outputNodes))

for i in outputNodes:
    print(i.nodeName)
    print(len(i.streetdata))
    for j in i.streetData:
        print(j[0],j[1])




# out= '''3
# 1
# 2
# rue-d-athenes 2
# rue-d-amsterdam 1
# 0
# 1
# rue-de-londres 2
# 2
# 1
# rue-de-moscou 1'''
# print(out)