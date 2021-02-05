arr=[4,5,6,7,8,9,10,12,13,14,15]
a=0
b=len(arr)-1
mid=0
if len(arr)-1 != arr[len(arr)-1]-arr[0]:
    while b>a+1:
        mid=(b+a)//2
        if (arr[a]-a-arr[0]) != (arr[mid]-mid-arr[0]):
            b=mid
        elif (arr[b]-b-arr[0]) != (arr[mid]-mid-arr[0]):
            a=mid
    print("Element is:", str(arr[mid]+1))
else:
    print("all elements are present")