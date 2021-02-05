class matrix:
    my_matrix=[]
    no_row=0
    no_row=0
    no_values=0
    def __init__(self,no_row,no_column,no_values):
        self.no_row=no_row
        self.no_column=no_column
        self.no_values=no_values
        
    def input_val(self):
        print("Input in form\nRow  Column  Value")    
        for v in range(self.no_values):
            k=input().split()
            k[0]=int(k[0])
            k[1]=int(k[1])
            k[2]=int(k[2])

            self.my_matrix.append(k)
        for p in self.my_matrix:print(p)

    def replace_at_pos(self,r,c,v,my_matrix_trans,pos):
        my_matrix_trans[pos]=[r,c,v]
    
    def Transpose(self):
        count=[0]*self.no_column
        for c in self.my_matrix:
            count[c[1]]+=1
        index=[0]*self.no_column
        for i in range(self.no_column-1):
            index[i+1]=index[i]+count[i]
        my_matrix_trans=[[0,0,0]]*self.no_values

        for c in range(self.no_values):
            pos=index[self.my_matrix[c][1]]
            self.replace_at_pos(self.my_matrix[c][1],self.my_matrix[c][0],self.my_matrix[c][2],my_matrix_trans,pos)
            index[self.my_matrix[c][1]]+=1
        self.my_matrix=my_matrix_trans
    
    def sum_matrix(self,matrix_B):
        sum_matrix=[0,0,0]*(self.no_values+matrix_B.no_values)
        i=0
        j=0
        while True:
            if len(self.my_matrix)==0:
                break
            elif len(matrix_B.my_matrix)<i+2:
                i=0
                sum_matrix[j]=self.my_matrix[0]
                self.my_matrix.remove(self.my_matrix[0])
                j+=1
                continue
            elif self.my_matrix[0][0]==matrix_B.my_matrix[i][0] and self.my_matrix[0][1]==matrix_B.my_matrix[i][1]:
                sum_matrix[j]=self.my_matrix[0]
                sum_matrix[j][2]=self.my_matrix[0][2]+matrix_B.my_matrix[i][2]
                self.my_matrix.remove(self.my_matrix[0])
                matrix_B.my_matrix.remove((matrix_B.my_matrix[i]))
                i=0
                j+=1
            else:i+=1
        k=j
        while True:
            if len(matrix_B.my_matrix)>0:
                sum_matrix[j]=matrix_B.my_matrix[0]
                print(matrix_B.my_matrix[0])
                matrix_B.my_matrix.pop(0)
                j+=1
            else:
                break
        sum_matrix=sum_matrix[0:j]
        self.my_matrix=sum_matrix
    
    def length_my_matrix(self):
        print(len(self.my_matrix))

    def print_matrix(self):
        for m in self.my_matrix:
            print(m)

def multiplication(matrix_A,matrix_B,matrix_C):
    c=0
    for i1 in matrix_A.my_matrix:
        for i2 in matrix_B.my_matrix:
            if i1[1]==i2[1]:
                k=c
                matrix_C.my_matrix.append([0,0,0])
                for l in matrix_C.my_matrix:
                    if l[0]==i1[0] and l[1]==i2[0] and l[2]!=0:
                        k=matrix_C.my_matrix.index(l)
                        matrix_C.my_matrix.remove([0,0,0])
                        c-=1
                        break
                matrix_C.my_matrix[k][0]=i1[0]
                matrix_C.my_matrix[k][1]=i2[0]
                matrix_C.my_matrix[k][2]+=i1[2]*i2[2]
                c+=1


switch=int(input("1) Transpose of a matrix\n2) Addition of two matrices\n3) Multiplication of two matrices\n"))
if switch==1:
    #lenMatrix=int(input("total number of elements in matrix: "))
    #I=int(input("Enter No of rows in matrix: "))
    #J=int(input("Enter No of Column in matrix: "))
    
    lenMatrix=10
    I=6
    J=9
    matrix_A=matrix(I,J,lenMatrix)
    # matrix_A.input_val()
    matrix_A.my_matrix=[
        [0,0,10],
        [0,7,20],
        [1,6,40],
        [2,5,90],
        [3,3,40],
        [4,8,30],
        [5,2,60],
        [4,7,50],
        [6,2,90],
        [5,6,70]
        ]
    matrix_A.Transpose()
    matrix_A.print_matrix()
elif switch==2:
    #I=int(input("Enter No of rows: "))
    #J=int(input("Enter No of Column: "))
    #lenMatrix_A=int(input("total number of elements in matrix_A: "))
    #lenMatrix_B=int(input("total number of elements in matrix_B: "))
    lenMatrix_A=3
    lenMatrix_B=5
    I=4
    J=5
    matrix_A=matrix(I,J,lenMatrix_A)
    matrix_B=matrix(I,J,lenMatrix_B)
    matrix_A.my_matrix=[
        [0,0,10], #111
        [0,7,20],
        [1,6,40],
        [2,5,90],
        [3,3,40]
        ]
    matrix_B.my_matrix=[
        [1,6,30],
        [0,7,60],
        [3,3,50],
        [6,2,90], #1111
        [2,5,70],
        [2,3,12333]
    ]

    matrix_A.sum_matrix(matrix_B)
    matrix_A.print_matrix()
elif switch==3:
    #I_A=int(input("Enter No of rows in matrix_A: "))
    #J_A=int(input("Enter No of Column in matrix_A: "))
    #I_B=int(input("Enter No of rows in matrix_B: "))
    #J_B=int(input("Enter No of Column in matrix_B: "))
    #lenMatrix_A=int(input("total number of elements in matrix_A: "))
    #lenMatrix_B=int(input("total number of elements in matrix_B: "))
    I_A=4
    J_A=4
    I_B=4
    J_B=5
    lenMatrix_A=4
    lenMatrix_B=5
    matrix_A=matrix(I_A,J_A,lenMatrix_A)
    matrix_B=matrix(I_B,I_B,lenMatrix_B)
    matrix_C=matrix(I_A,I_B,I_A*I_B)
    matrix_A.my_matrix=[
        [0,1,10],
	    [0,2,12],
	    [1,0,1],
	    [1,2,2]]
    matrix_B.my_matrix=[
        [0,0,2],
        [0,1,5],
	    [1,1,1],
	    [2,0,8],
	    [2,1,3]
    ]
    if I_B!=J_A:
        print("Matrix's dimensions not satisfied")
    else:
        matrix_B.Transpose()
        multiplication(matrix_A,matrix_B,matrix_C)
        matrix_C.print_matrix()
else: print("'%d' Not valid"%(switch))