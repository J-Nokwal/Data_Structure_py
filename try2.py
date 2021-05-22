
def position(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]==0):
                return [i,j]



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

ar=[[1,2,3],
    [4,0,5],
    [6,7,8]]

goal=[[1,2,3],
      [0,4,5],
      [6,7,8]]

state=[]
state.append(ar)
visited=[]

visited.append(ar)
#arr=copy.deepcopy(ar)
pos=position(ar)

count=0
while(ar!=goal):    
    ar=state.pop(0)
    count+=1
    print(ar)
    pos=position(ar)
    
    # ar_up=up(pos,ar)
    # print("kkkk",ar_up not in visited)
    if(up(pos,ar) not in visited):
        # print(ar_up)
        state.append(up(pos,ar))
        visited.append(up(pos,ar))
    
    # ar_down=down(pos,ar)
    elif(down(pos,ar) not in visited):
        #print(ar_down)
        state.append(down(pos,ar))
        visited.append(down(pos,ar))
   
    # ar_left=left(pos,ar)
    elif(left(pos,ar) not in visited):
        #print(ar_left)
        state.append(left(pos,ar))
        visited.append(left(pos,ar))
    
    # ar_right=right(pos,ar)
    elif(right(pos,ar) not in visited):
        # print(ar_right)
        state.append(right(pos,ar))
        visited.append(right(pos,ar))
    else:
        break
    
    
if(ar==goal):
    print("Reached")
    print(count)
else:
    print("Not possible")
