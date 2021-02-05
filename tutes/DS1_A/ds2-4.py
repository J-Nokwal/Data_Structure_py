def saddle(matrix):
    i=len(matrix)
    j=len(matrix[0])
    saddle_i=0
    saddle_j=0
    k=False
    for row in range(i):
        saddle=matrix[row][0]
        for column in range(j):
            if saddle>=matrix[row][column]:
                saddle=matrix[row][column]
                saddle_i=row
                saddle_j=column
        for row_1 in range(i):
            if saddle<matrix[row_1][saddle_j]:
                saddle=False
                break
        if saddle!=False:
            print("%d at [%d*%d] is minimum in its row and maximum in its column."%(saddle,saddle_i,saddle_j))
            k=True
    if k==False: print("No saddle point")

mat=[[9,2,3],
    [2,6,4],
    [4,5,4]]
mat=[[1, 2, 3],
    [10, 11, 9],
    [4, 5, 6]]
saddle(mat)