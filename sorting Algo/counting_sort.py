def countingsort(arr):
    min_element=min(arr)
    max_element=max(arr)
    output_arr=arr[:]
    count_arr=[0]*(max_element-min_element+1)
    
    for i in arr:
        # print(i)
        count_arr[i-min_element]+=1
    
    print(count_arr)
    for i in range(1,len(count_arr)):
        count_arr[i]+=count_arr[i-1]
    print(count_arr)

    # for i in range(len(arr)-1, -1, -1):
    #     output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
    #     count_arr[arr[i] - min_element] -= 1

    for i in range(len(arr)):
        output_arr[count_arr[arr[i]-min_element]-1]=arr[i]
        count_arr[arr[i] - min_element] -= 1
    return output_arr
    # print(len(count_arr))

arr = [1,4,1,2,7,5,2] 
#arr=[1,2,3,4,5,6,7,9,8]
n = len(arr) 
arr=countingsort(arr) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=" ")