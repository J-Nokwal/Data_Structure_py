X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
k=0
for k in range(len(X)):
    for i in range(len(Y[0])):
        for j in range(len(X[0])):
            result[k][i] = result[k][i] + X[k][j]*Y[j][i]
            
for l in result:
    print(l)