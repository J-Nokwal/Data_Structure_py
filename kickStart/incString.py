def fxn(s,i):
    s='DCD'
    count=1
    last=ord(s[0])
    print('Case #{}:'.format(i+1),end=" ")
    for i in s:
        temp=ord(i)
        # print('kkkk',temp)
        if last<temp:
            count+=1
        else:
            count=1

        last=temp
        print(count,end=" ")
    print()
        # if count==1:
            # print("1",end=" ")
            # count+=1
        

# n=int(input())
arr=[]
# for i in range(n):
    # l=int(input())
    # s=input()
    # arr.append([l,s])
# 
# for i in range(len(arr)):
    # fxn(arr[i][1],i)

    
fxn('dds',1)