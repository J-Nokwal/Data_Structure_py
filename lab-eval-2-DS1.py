
def boundry_validation(sq, to_check):
    if sq in boundry_check:
        return to_check in boundry_check[sq]
    else:
        return True

def move_crr(crr,direction):
    return (crr + movement[direction][0]*size[1] + movement[direction][1] ) 

def algo(gpath,crr,complete=False):
    path = gpath[:]
    
    if crr not in path:
        path.append(crr)
    else:
        return (gpath, complete)

    if crr == size[0]*size[1]:
        return (path,True)
    
    for i in range(4):
        next_path = move_crr(crr,i)
        if not complete and data[crr][i]==1 and boundry_validation(crr,i):
            gpath,complete = algo(path,next_path,complete)
    
    return (gpath,complete)




movement= {
    0: [-1, 0], #up
    1: [0, 1], #right
    2: [1, 0], #down
    3: [0, -1] #left
}
    


#input values
size = list(map(int, input().split()))
data= {}
for i in range(size[0]*size[1]):
    k= list(map(int, input().split()))
    data[k[0]]= k[1:]
path=[]

boundry_check={
    1: [1, 2],
    size[0]*size[1]: [3, 0],
    size[0]*(size[1]-1)+1: [0, 1],
    size[1]: [3, 2],
}

for i in range(2, size[1]):
    boundry_check[i]= [1, 2, 3]
for i in range(size[1]+1, size[0]*(size[1]-1)+1, size[1]):
    boundry_check[i]= [0, 1, 2]
for i in range(2*size[1], size[1], size[1]):
    boundry_check[i]= [0, 2, 3]
for i in range(size[0]*(size[1]-1)+2, size[0]*size[1]):
    boundry_check[i]= [0, 1, 3]
    
# recursion starting point 
final= algo(path, 1)[0]

#print answer
for i in final:
    print(i,end=" ")