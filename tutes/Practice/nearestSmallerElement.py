class Stack1():
    def __init__(self,maxSize):
        self.top=0
        self.maxSize=maxSize
        self.stack=[]

    def push(self,data):
        if self.top<self.maxSize:
            self.stack[top+1]=data
        else:print("Stack Overflow")

    def peek(self):
        if self.top==0:
            print("Stack is empty")
            return False 
        return self.stack[self.top]
    
    def pop(self):
        k=self.peek():
        if not k:
            self.stack.remove(k)

