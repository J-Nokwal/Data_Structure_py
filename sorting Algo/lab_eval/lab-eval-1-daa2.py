import numpy as np
# m,n=map(int, input().split())
# a=input()
# m,n=4,4
# a='18 4 16 8 23 13 20 11 28 24 26 25 1 30 15 19'
m,n=3,2
a='65 7 5 33 9 3'
# m,n=5,5
# a='10 8 69 50 30 5 20 100 1 0 80 55 60 120 1000 4 15 25 2 3 6 56 66 65 105'
# m,n=3,3
# a='18 9 11 1 4 15 13 23 20'
arr=np.fromstring(a, dtype=np.int16, sep=' ')
arr.resize(m,n)
# print(arr)

def mergeSort(arr):
    c=arr.size
    if c>1:
        mid = c//2
        left=arr[:mid].copy()
        right=arr[mid:].copy()
        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while i<left.size and j<right.size:
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        
        while i<left.size:
            arr[k]=left[i]
            i+=1
            k+=1
        
        while j<right.size:
            arr[k]=right[j]
            j+=1
            k+=1
        print(arr)

def mergesort2D(arr):
    a,b=arr.shape
    if a>1 or b>1:
        
        midH=int(np.ceil(a/2))
        midV=int(np.ceil(b/2))
        # upperLeft=arr[:midV,:midH]
        # upperRight=arr[:midV,midH:]
        # lowerLeft=arr[midV:,:midH]
        # lowerRight=arr[midV:,midH:]
        upperLeft=arr[:midH,:midV]
        upperRight=arr[:midH,midV:]
        lowerLeft=arr[midH:,:midV]
        lowerRight=arr[midH:,midV:]
        print(arr)
        mergesort2D(upperLeft)
        mergesort2D(upperRight)
        mergesort2D(lowerLeft)
        mergesort2D(lowerRight)

        for k in arr:
            
            mergeSort(k)
            # k.sort()
        arr=arr.T
        for k in arr:
            mergeSort(k)
            # k.sort()
        arr=arr.T
print(arr)
mergesort2D(arr)

# print(arr)
for i in arr.ravel():
    print(i,end=' ')
print()
print(arr)