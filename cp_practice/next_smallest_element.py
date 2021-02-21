def nge(arr,n):
    stack=[n-1]
    rb=[None for i in range(n)]
    rb[-1]=n
    for i in range(n-2,-1,-1):
        while(len(stack)>0 and arr[stack[-1]]>arr[i]):
            stack.pop()
        
        if len(stack)==0:
            rb[i]=n
        else:
            rb[i]=stack[-1]
        stack.append(i)
    for i in range(n):
        if rb[i]==n:
            print(-1,end=" ")
        else: print(arr[rb[i]],end=" ")



a=[11, 13, 2,21, 3,4]
n=len(a)
nge(a,n)