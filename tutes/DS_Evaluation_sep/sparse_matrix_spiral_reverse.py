class spiral_cheak:
    
    altercount=1  # times iterate in specific direction

    def main_code(self,info,data,start):
        # code
        self.i=start[0]
        self.j=start[1]
        self.ii=info[0]
        self.jj=info[1]
        self.data=data
        self.info=info
        self.start=start
        for spa in self.data:
                if spa[0]==self.i and spa[1]==self.j:
                    print(spa[0],spa[1],spa[2],"1")
        while(True):
            # Down funtion
            if not self.i+self.altercount<self.ii:
                print("break down")
                break
            self.downCheak()
            # Right function
            if not self.j+self.altercount<self.jj:
                print("break right")
                break
            self.rightCheak()
            self.altercount+=1
            # Up Function
            if not self.i-self.altercount>=-1:
                print("break up")
                break
            self.upCheak()
            # Left Function
            if not self.j-self.altercount>=-1:
                print("break left")
                break
            self.leftCheak()
            self.altercount+=1

    def downCheak(self):
        i=self.i
        print("34342k",i+self.altercount)
        while(self.i<i+self.altercount):
            self.i+=1
            print("1111k,down",self.i,self.j)
            # here while loop to cheak if i,j present in matrix
            for spa in self.data:
                if spa[0]==self.i and spa[1]==self.j:
                    print(spa[0],spa[1],spa[2],"1")
            
            
    def rightCheak(self):
        j=self.j
        while(self.j<j+self.altercount):
            self.j+=1
            print("2222k,right",self.i,self.j)
            # here while loop to cheak if i,j present in matrix
            for spa in self.data:
                if spa[0]==self.i and spa[1]==self.j:
                    print(spa[0],spa[1],spa[2],"2")
            

    def upCheak(self):
        i=self.i
        print("upupup",i,self.altercount,i-self.altercount)
        while(self.i>i-self.altercount):
            self.i-=1
            print("3333k,up",self.i,self.j)
            # here while loop to cheak if i,j present in matrix
            for spa in self.data:
                if spa[0]==self.i and spa[1]==self.j:
                    print(spa[0],spa[1],spa[2],"3")
            

    def leftCheak(self):
        j=self.j
        while(self.j>j-self.altercount):
            self.j-=1
            print("44444k,left",self.i,self.j)
            # here while loop to cheak if i,j present in matrix
            for spa in self.data:
                if spa[0]==self.i and spa[1]==self.j:
                    print(spa[0],spa[1],spa[2],"4")
            


# input data
info= list(map(int, input().split()))
data=[]
for i in range(info[2]):
    data.append(list(map(int, input().split())))
start=list(map(int,input().split()))

spiral=spiral_cheak()
spiral.main_code(info,data,start)
