def bubbleSort(arr):
    n=len(arr)
    #c=0
    for i in range(n-1):
        flag=0
        for j in range(n-i-1):
            #c+=1
            if arr[j]>arr[j+1]:
                flag=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if flag==0:break
        # print("pass",i,"count",c)
    


arr =[64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
for i in arr:
    print(i,end=" ")