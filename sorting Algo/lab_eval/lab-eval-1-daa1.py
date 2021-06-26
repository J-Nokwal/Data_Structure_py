minMarks,students,questions = map(int, input().split()) # minMarks,S,N
stuMarks=list(map(int,input().split()))
qList=[]
for i in range(questions):
    qList.append(list(map(int,input().split()))+[i+1])

# minMarks,students,questions=75 ,3 ,5
# stuMarks=[15 ,50 ,35]
# qList=[
#    [6, 3,1],[11, 1,2], [13, 4,3],[27, 1,4],[18, 2,5],]


# print(qList)
qList.sort(key=lambda x:x[1],reverse=True)

# print(qList)

        

i=0

while( i < (questions-1)):
    if qList[i][1]==qList[i+1][1]:
        temp=i
        while(qList[temp][1]==qList[temp+1][1]):
            temp+=1
            if temp==questions-1:
                break
        qList[i:temp+1]=sorted(qList[i:temp+1],key=lambda x:x[0])
        i=temp
    i+=1
# print(qList)
for i in stuMarks:
    a=[]
    total=i
    temp=0
    while(total<minMarks):
        temp2=qList[temp]
        total+=temp2[0]
        temp+=1
        a.append(temp2[2])
    print(len(a),end=' ')
    for j in sorted(a):
        print(j,end=' ')
    print()




# print(qList,type(qList[0][1]))
# print(minMarks,type(minMarks)) 
# print(stuMarks,type(stuMarks[0]))
