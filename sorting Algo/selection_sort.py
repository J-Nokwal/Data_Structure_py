
def selectionSort(A):

    for i in range(len(A)):
        min_no=i
        for j in range(i+1,len(A)):
            if A[min_no]>A[j]:
                min_no=j
        A[min_no],A[i]=A[i],A[min_no]


A = [64, 25, 12, 22, 11] 

selectionSort(A)
print(A)