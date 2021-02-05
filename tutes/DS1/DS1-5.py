my_list=[1,2,3,12,34,46,64,67,86,89,90,99]
x=int(input("Number to be searched: "))
a=0
b=len(my_list)-1
while True:
    if a<=b:
        mid = a + (b - a) // 2
        print(mid)
        if x==my_list[mid]:
            print("Found at index: "+str(mid))
            break
        elif x<my_list[mid]:
            b=mid-1
            continue
        elif x>my_list[mid]:
            a=mid+1
            continue
    else:
        print("Number not found")
        break