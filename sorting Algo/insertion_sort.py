def InsertonSort(arr):
    n=len(arr)
    # c=0
    for i in range(1,n):
        for j in range(i,0,-1):
            # print(j)
            # c+=1
            if arr[j]<arr[j-1]:
                # print("yes")
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                # print("no" )
                break
    # print(i,c)



arr =[64, 34, 25, 12, 22, 11, 9,76,8,0]
InsertonSort(arr)
for i in arr:
    print(i,end=" ")