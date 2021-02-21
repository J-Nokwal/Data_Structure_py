def push(s,x):
    s.append(x)
def pop(s):
    return s.pop()
def isEmpty(s):
    return len(s)==0
def isFull(s,n):
    return len(s)>=n
def insertAtEnd(s,x):
    if isEmpty(s):
        push(s,x)
    else:
        temp=pop(s)
        insertAtEnd(s,x)
        push(s,temp)
def reverse(s):
    if not isEmpty(s):
        temp=pop(s)
        reverse(s)
        insertAtEnd(s,temp)


stack = []
push( stack, str(4) ) 
push( stack, str(3) ) 
push( stack, str(2) ) 
push( stack, str(1) ) 
print(stack)
print("reversed Stack ") 
reverse(stack) 
print(stack)
