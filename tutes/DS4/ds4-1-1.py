class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize

    size = -1
    stk = []

    def safe(self):
        #print(self.size)
        if self.size == -1:
            #print("111lk")
            return 0
        elif self.size >= self.maxSize-1:
            return 1
        else:
            return -1

    def push(self, data):
        if (self.safe() == 1):
            print('Over Flow')
        else:
            self.stk.append(data)            
            self.size += 1
        #print(self.stk)

    def pop(self):
        if (self.safe() == 0):
            print("Under Flow")
        else:
            self.stk.remove(self.stk[self.size])  # self.stk.pop()
            self.size -= 1

    def isFull(self):
        if (self.safe() == 1):
            print("Stack is Full")
        else:
            print("Stack is not Full")

    def isEmpty(self):
        if (self.safe() == 0):
            print("Stack is Empty")
        else:
            print("Stack is not Empty")

    def peek(self):
        if (self.safe() == 0):
            print("Stack is Empty")
        else:
            print(self.stk[self.size])

    def display(self):
        top = self.size+1
        #print("topp",top)
        for i in range(top):
            # print("top-i-1: ",top-i-1)
            print(self.stk[top-i-1],end=" ")
        print()


newstack = Stack(int(input("Enter max Size of Stack: ")))
#newstack = Stack(3)
print(("----------------------\n1. Push\n2. pop\n3. isEmpty?\n4. isFull?\n5. Peek\n6. Display\n7. End operations\n"))
while (True):
    #k = int(input("----------------------\n1. Push\n2. pop\n3. isEmpty?\n4. isFull?\n5. Peek\n6. Display\n7. End operations\n"))
    k=int(input())
    if k == 1:
        # print("kkk-1")
        m = int(input("Enter Data to push: "))
        newstack.push(m)
    elif k == 2:
        newstack.pop()
    elif k == 3:
        newstack.isEmpty()
    elif k == 4:
        newstack.isFull()
    elif k == 5:
        newstack.peek()
    elif k == 6:
        newstack.display()
    elif k == 7 :
        break
# newstack.isFull()
# newstack.push(4)
# newstack.push(3)
# newstack.push(5)
# newstack.pop()
# #newstack.peek()
# newstack.push(7)
# newstack.push(8)
# newstack.push(990)
# newstack.isFull()
# print(newstack.stk)
# newstack.display()