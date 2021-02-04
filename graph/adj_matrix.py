
def adj_matrix(a,v):
    mat=[[0]*v for i in range(v)]
    # for i in range(v):
    #     mat.append([0]*v)
    
    for i in a:
        print(i[0],i[1])
        mat[i[0]][i[1]]=1
        mat[i[1]][i[0]]=1
    
    for i in mat:
        print(i)

a=[
    [0,1],
    [0,4],
    [1,2],
    [1,3],
    [1,4],
    [2,3],
    [3,4]
    ]

v=5 # no of node (vertices)
adj_matrix(a,v)
