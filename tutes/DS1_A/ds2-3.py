def sum_row(matrix):
    i=0
    j=len(matrix[0])
    for l in matrix:
        sum_1=0
        for m in range(j):
            sum_1+=l[m]
        i+=1
        print("sum of row %d: %d"%(i,sum_1))

def sum_column(matrix):
    h=len(matrix[0])
    for i in range(h):
        sum_1=0
        for j in matrix:
            sum_1+=j[i]            
        print("Sum of Column %d: %d"%(i+1,sum_1))

mat=([
    [9,2,3],
    [2,6,4],
    [4,5,4]
    ])
sum_row(mat)
sum_column(mat)