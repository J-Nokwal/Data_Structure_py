
def countingSort(arr,exp):
    a=[(i%(exp*10))//exp for i in arr]
    
    b=[0]*10
    print(a)
    for i in a:
        b[i]+=1
    
    for i in range(1,10):
        b[i]+=b[i-1]
    
    for i in range(len(arr)-1,-1,-1):
        a[b[(arr[i]%(exp*10))//exp]-1] = arr[i]
        b[(arr[i]%(exp*10)//exp)]-=1
    return a



def radixSort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1 // exp > 0: 
        #print(exp)
        arr=countingSort(arr, exp) 
        exp *= 10
    return arr



arr = [170, 45, 75, 90, 802, 24, 2, 66] 
arr=radixSort(arr) 
for i in range(len(arr)): 
    print(arr[i],end=" ")