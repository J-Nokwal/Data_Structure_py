
def maxheap(arr,n,i):
    left=i*2+1
    right=i*2+2
    largest=i
    
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest is not i:
        arr[i],arr[largest]=arr[largest],arr[i]
        maxheap(arr,n,largest)


def heapSort_inc(arr,n):
    for i in range(n//2-1,-1,-1):
        maxheap(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        maxheap(arr,i,0)

def minheap(arr,n,i):
    left=i*2+1
    right=i*2+2
    smallest=i
    
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest is not i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        minheap(arr,n,smallest)


def heapSort_dec(arr,n):

    for i in range(n//2-1,-1,-1):
        minheap(arr,n,i)

    for i in range(n-1,0,-1):

        arr[i],arr[0]=arr[0],arr[i]
        minheap(arr,i,0)

def extract_max(arr,n):
    a=arr[:]
    for i in range(n//2-1,-1,-1):
        maxheap(a,n,i)
    print("\n111k",a[0])

def extract_min(arr,n):
    a=arr[:]
    for i in range(n//2-1,-1,-1):
        minheap(a,n,i)
    print("222k",a[0])

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
heapSort_inc(arr,n)
print("Sorted array in inc order is")
for i in range(n):
    print("%d" % arr[i],end=" "),
print()

heapSort_dec(arr,n)
print("Sorted array in dec order is")
for i in range(n):
    print("%d" % arr[i],end=" "),

extract_max(arr,n)
extract_min(arr,n)