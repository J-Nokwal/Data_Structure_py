class stack:
    stk=[]
    def __init__(self,string):
        for i in string:
            if i==' ':
                continue
            self.stk.append(i)
    def display(self):
        size=len(self.stk)
        for i in range(size):
            print(self.stk[size-i-1],end="")
        print()

newStack=stack(input("Enter string: "))
newStack.display()