class spiral:

    def printSpiral(self,matrix,l,m,count):
        self.matrix=matrix
        if l>=m:
            return
        for p in range(l,m):
            self.matrix[l][p]=count
            count+=1
           
        for p in range(l + 1,m):
            self.matrix[p][m-1]=count
            count+=1
            
        if ((m - 1) != l): 
            for p in range(m - 2, l - 1, -1):
                self.matrix[m-1][p]=count
                count+=1 
                
        if ((m - 1) != l): 
            for p in range(m - 2, l, -1):
                self.matrix[p][l]=count+1
                count+=1 
        self.printSpiral(matrix, l + 1, m - 1,count) 

    
k=5
arr=[]
for l in range(k):
    arr.append([0]*k)    

obj=spiral()
obj.printSpiral(arr,0,k,1)

for l in obj.matrix:
    print(l)
    
# 0  1  2  3  4
# 15 16 17 18 5
# 14 23 24 19 6
# 13 22 21 20 7
# 12 11 10 9  8