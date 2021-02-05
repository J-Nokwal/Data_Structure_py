x=int(input("Enter size of Diagonal Matrix: "))
arr=[]
for k in range(x):
    temp=[]
    for l in range(x):
        temp.append(0)
    arr.append(temp)


def diagonal():
    for k in range(x):
        arr[k][k]=int(input("Enter value at %d*%d: "%(k, k)))

def trigonal():
    for i in range(x): 
        for j in range(x):
            if abs(i-j) <=1:
                arr[i][j]=int(input("Enter value at %d*%d: "%(i+1, j+1)))     

def lower_tri():
    for i in range(x): 
        for j in range(x):
            if not j>i:
                arr[i][j]=int(input("Enter value at %d*%d: "%(i+1, j+1)))     

def upper_tri():
    for i in range(x): 
        for j in range(x):
            if not i>j:
                arr[i][j]=int(input("Enter value at %d*%d: "%(i+1, j+1)))     

def Symmetric_matrix():
    for i in range(x): 
        for j in range(x):
            if i==j:
                arr[i][i]=int(input("Enter value at %d*%d: "%(i+1, i+1)))

            if not i>j and i!=j:
                arr[i][j]=int(input("Enter value at %d*%d and at %d*%d: "%(i+1, j+1,j+1,i+1)))     
                arr[j][i]=arr[i][j]

toDo=int(input("1) Diagonal Matrix\n2) Tri-diagonal Matrix\n3) Lower triangular Matrix\n4) Upper triangular Matrix\n5) Symmetric Matrix\n"))

if toDo==1:diagonal()
elif toDo==2:trigonal()
elif toDo==3:lower_tri()
elif toDo==4:upper_tri()
elif toDo==5:Symmetric_matrix()
else:print("invalid inputt")

for l in arr:print(l)
