def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        



# arr =[64, 34, 25, 12, 22, 11, 9,76,8,1]
# arr = [12, 11, 13, 5, 6, 7]
arr=[18,4]
mergeSort(arr)
for i in arr:
    print(i,end=" ")