arr=[64,34,25,12,22,11,90]
for k in range(len(arr)):
    i=k-1
    while True:
        if arr[i]>arr[i+1] and i!=-1:
            #print(i,arr[i],i+1,arr[i+1])
            arr[i], arr[i+1] = arr[i+1], arr[i] 
            i=i-1            
        else:
            break
print(arr)