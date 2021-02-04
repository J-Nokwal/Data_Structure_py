def search(arr,x,n):
    for i in range(x):
        if arr[i]==x:
            return i
    return -1

arr = [2, 3, 4, 10, 40] 
x = 10
n = len(arr) 

k= search(arr,x,n)
if k==-1:
    print("Element is not present")
else:
    print ("Element is present at index {} and is {}".format(k,arr[k]))