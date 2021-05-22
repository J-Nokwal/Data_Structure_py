def transfer(j1,j2,max1,max2):
    if(j1+j2>max1):
        j2=j1+j2-max1
        j1=max1
    else:
        j1=j1+j2
        j2=0
    return [j1,j2]
    
    
def fill(container,max1):
    container=max1
    return container
    
    
    
def empty(container):
    container=0
    return container


pair=[0,0]
goal=[0,2]
state=[]
visited=[]
state.append(pair)
visited.append(pair)
max1=int(input("Enter the max amount of water jug 1 can hold:"))
max2=int(input("Enter the max amount of water jug 2 can hold:"))
count=0
while(pair!=goal):
    
    pair=state.pop(0)
    
    fill_1=pair[:]
    fill_1[0]=fill(pair[0],max1)
    if(fill_1==goal):
        print("Goal state reached {} fill".format(fill_1))
        break
    if(fill_1 not in visited):
        visited.append(fill_1)
        state.append(fill_1)
  
    fill_2=pair[:]
    fill_2[1]=fill(pair[1],max2)
    if(fill_2==goal):
        print("Goal state reached {} fill".format(fill_2))
        break
    if(fill_2 not in visited):
        visited.append(fill_2)
        state.append(fill_2)
    
    transfer_1=transfer(pair[0],pair[1],max1,max2)
    if(transfer_1==goal):
        print("Goal state reached {} transfer".format(transfer_1))
        break
    if(transfer_1 not in visited):
        visited.append(transfer_1)
        state.append(transfer_1)
    
    transfer_2=transfer(pair[1],pair[0],max2,max1)
    transfer_2.reverse()
    if(transfer_2==goal):
        print("Goal state reached {} transfer".format(transfer_2))
        break
    if(transfer_2 not in visited):
        visited.append(transfer_2)
        state.append(transfer_2)
        
    empty_1=pair[:]
    empty_1[0]=empty(pair[0])
    if(empty_1==goal):
        print("Goal state reached {} empty".format(empty_1))
        break
    if(empty_1 not in visited):
        visited.append(empty_1)
        state.append(empty_1)
    
    empty_2=pair[:]
    empty_2[1]=empty(pair[1])
    if(empty_1==goal):
        print("Goal state reached {} empty".format(empty_1))
        break
    if(empty_2 not in visited):
        visited.append(empty_2)
        state.append(empty_2)
    
print(pair)
