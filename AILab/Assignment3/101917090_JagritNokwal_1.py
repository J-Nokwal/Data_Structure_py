# State search with Best First Search algorithm Heuristic search

def position(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]==0):
                return [i,j]

def heuristic_fxn(arr):
    c=0
    for i in range(3):
        for j in range(3):
            if arr[i][j]==end[i][j]:
                if arr[i][j]==0:
                    continue
                c+=1
    return c

def up(pos,ar):
    s= [i[:] for i in ar]
    if(pos[0]>0):
        s[pos[0]-1][pos[1]],s[pos[0]][pos[1]]=s[pos[0]][pos[1]],s[pos[0]-1][pos[1]]
    return s


def down(pos,ar):
    s= [i[:] for i in ar]
    if(pos[0]<len(s)-1):
        s[pos[0]+1][pos[1]],s[pos[0]][pos[1]]=s[pos[0]][pos[1]],s[pos[0]+1][pos[1]]
    return s;


def left(pos,ar):
    s= [i[:] for i in ar]
    if(pos[1]>0):
        s[pos[0]][pos[1]-1],s[pos[0]][pos[1]]=s[pos[0]][pos[1]],s[pos[0]][pos[1]-1]
    return s


def right(pos,ar):
    s= [i[:] for i in ar]
    if(pos[1]<len(s[0])-1):
        s[pos[0]][pos[1]+1],s[pos[0]][pos[1]]=s[pos[0]][pos[1]],s[pos[0]][pos[1]+1]
    return s;

# crr=start=[[2,0,3],[1,8,4],[7,6,5]]
# end=[[1,2,3],[8,0,4],[7,6,5]]
crr=[[2,8,3],[1,5,4],[7,6,0]]
end=[[1,2,3],[8,0,4],[7,6,5]]
prep_seq=[crr]
count=0
while crr != end:
    temp=[0,0,0,0] # up down left right
    temp2=[0,0,0,0]
    # par=heuristic_fxn(crr)
    pos=position(crr)

    # Try every state
    t=up(pos,crr)
    if t != crr:
        temp[0]=heuristic_fxn(t)
        temp2[0]=t
        # print(heuristic_fxn(t),end=" 0  ")
    t=down(pos, crr)
    if t != crr:
        temp[1]=heuristic_fxn(t)
        temp2[1]=t
        # print(heuristic_fxn(t),end=" 1  ")
    t=left(pos,crr)
    if t != crr:
        temp[2]=heuristic_fxn(t)
        temp2[2]=t
        # print(heuristic_fxn(t),end=" 2  ")
    t=right(pos,crr)
    if t != crr:
        temp[3]=heuristic_fxn(t)
        temp2[3]=t
        # print(heuristic_fxn(t),end=" 3  ")
    
    #Check for valid state
    a=temp.index(max(temp))
    while temp2[a] in prep_seq:
        temp[a]=0
        a=temp.index(max(temp))
    crr=temp2[a]
    prep_seq.append(crr)

    if temp==[0,0,0,0]:
        break
    print(heuristic_fxn(crr))
    for i in crr:
        print(i)
    print() 
    # print(crr)

    count+=1

print(count,'no. of states needed to be change')