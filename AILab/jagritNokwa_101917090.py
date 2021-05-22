# State search with Best First Search algorithm Heuristic search
from random import shuffle

def position(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]==0):
                return [i,j]

def heuristic_fxn(arr,end):
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

def random_state():
    arr=list(range(9))
    shuffle(arr)
    st=[]
    for i in range(3):
        p=[]
        p.append(arr[(3*i)+0])
        p.append(arr[(3*i)+1])
        p.append(arr[(3*i)+2])
        st.append(p)
    return st

def HillClimb(start,end):
    prep_seq=[start]
    crr=start
    count=0
    pre_H_Val=heuristic_fxn(crr,end)
    while crr != end:
        temp=[0,0,0,0] # up down left right # stores H value
        temp2=[0,0,0,0] # stores State
        # par=heuristic_fxn(crr)
        pos=position(crr)

        # Try every state
        t=up(pos,crr)
        if t != crr:
            temp[0]=heuristic_fxn(t,end)
            temp2[0]=t
            # print(heuristic_fxn(t),end=" 0  ")
        t=down(pos, crr)
        if t != crr:
            temp[1]=heuristic_fxn(t,end)
            temp2[1]=t
            # print(heuristic_fxn(t),end=" 1  ")
        t=left(pos,crr)
        if t != crr:
            temp[2]=heuristic_fxn(t,end)
            temp2[2]=t
            # print(heuristic_fxn(t),end=" 2  ")
        t=right(pos,crr)
        if t != crr:
            temp[3]=heuristic_fxn(t,end)
            temp2[3]=t
            # print(heuristic_fxn(t),end=" 3  ")
        
        #Check for valid state
        a=temp.index(max(temp))

        if temp[a]<=pre_H_Val:  
            break
        pre_H_Val=temp[a]
        
        crr=temp2[a]
        prep_seq.append(crr)
        count+=1

    # print(count,'no. of states needed to be change')
    if crr==end:
        return (True,count,prep_seq)
    else : return False,count,prep_seq
    
no_of_init_states=0
while True:
    start=random_state()
    end=[[2,8,1],[0,4,3],[7,6,5]]
    flag,count,prep_seq=HillClimb(start, end)
    no_of_init_states+=1
    if flag:
        print("In State")
        for i in prep_seq[0]:
            print(i)
        print("{} no. of states needed to be change".format(count),end="\n\n")
        for j in prep_seq[1:]:
            for i in j:
                print(i)
            print() 
        break
print("no of iteration for this initial state",no_of_init_states)
