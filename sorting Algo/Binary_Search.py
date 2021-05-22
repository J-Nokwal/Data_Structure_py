    def binarySearch(arr,x,l,r):
    if r>=1:
        mid = (l+r)//2
        # mid = l + (r - l) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,x,l,mid-1)
        else:
            return binarySearch(arr,x,mid+1,r)
    else:
        return -1


arr = [0, 2, 4, 6, 8, 10, 12, 14, 16,18,20 ] 
# arr=list(map(int,input.split))

x = 20
  
# Function call 
result = binarySearch(arr,x,0,len(arr)-1)
print(result)
if result != -1: 
    print ("Element is present at index {}".format(result)) 
else: 
    print ("Element is not present in array")