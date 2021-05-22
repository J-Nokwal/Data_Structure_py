
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

goal=[[2,1,3],
      [4,0,5],
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
    
    ar_up=up(pos,ar)
    # print("kkkk",ar_up not in visited)
    if(ar_up not in visited):
        print("kkkk",ar_up not in visited)
        # print(ar_up)
        state.append(ar_up)
        visited.append(ar_up)
    
    ar_down=down(pos,ar)
    if(ar_down not in visited):
        print("ooooo",ar_down not in visited)
        #print(ar_down)
        state.append(ar_down)
        visited.append(ar_down)
   
    ar_left=left(pos,ar)
    if(ar_left not in visited):
        print("lllll",ar_left not in visited)
        #print(ar_left)
        state.append(ar_left)
        visited.append(ar_left)
    
    ar_right=right(pos,ar)
    if(ar_right not in visited):
        print("mmmmm",ar_right not in visited)
        # print(ar_right)
        state.append(ar_right)
        visited.append(ar_right)
    
    
if(ar==goal):
    print("Reached")
    print(count)
else:
    print("Not possible")
