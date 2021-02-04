
def partition(arr,low,high):
    pivot=arr[high]
    i=low
    for j in range(low,high):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i
            
def quickSort(arr,l,r):
    if l<r:
        p=partition(arr,l,r)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,r)


arr = [10, 7, 8, 9, 1, 3,55,2] 
arr=[1,2,3,4,5,6,7,9,8]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=" ")