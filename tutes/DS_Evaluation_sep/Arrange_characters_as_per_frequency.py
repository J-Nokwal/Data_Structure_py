def print1(data_list,dic):
    for i in data_list:
        print("{} {}".format(i,dic[i]),end=" ")
    print()

# def freq(string):
#     freq_data={}
#     for ch in string:
#         if ch in freq_data:
#             freq_data[ch]+=1
#         else:
#             freq_data[ch]=1
#     for k,v in freq_data.items():
#         print(k,v,end=" ")
#     print()
#     return freq_data
    
# def arrange(freq_data,N):
#     start=-1
#     endl=-1
#     new_data=freq_data
#     temp=None
#     for i in freq_data:
#         if i[1]==N and start!=-1:
#             endl=freq_data.index(i)+1
#         elif i[1]==N:
#             start=freq_data.index(i)
#     for i in freq_data[start:endl]:
#         if i[1]>N:
#             temp=i
#             new_data.remove(i)
#             new_data.append(temp)
#         elif i[1]<N:
#             temp=i
#             new_data.remove(i)
#             new_data.insert(0,temp)
#     for i in new_data:
#         print(i[0],i[1],end=" ")
#     print()
#     return new_data
def arrange(freq_data,N):
    data_list=freq_data
    temp=None
    a=[]
    for i in data_list:
        if data[i]==N:
            a.append(i)
    for i in freq_data[freq_data.index(a[0]):freq_data.index(a[-1])]: #cheak for problem here
        if data[i]==N:
            continue
        if data[i]>N:
            #at end
            temp=i
            data_list.remove(i)
            data_list.append(temp)
            continue
        if data[i]<N:
            #at beg
            temp=i
            data_list.remove(i)
            data_list.insert(0,i)
            continue
    return data_list

    # for i in freq_data[start:endl]:
    #     if i[1]>N:
    #         temp=i
    #         new_data.remove(i)
    #         new_data.append(temp)
    #     elif i[1]<N:
    #         temp=i
    #         new_data.remove(i)
    #         new_data.insert(0,temp)
    # for i in new_data:
    #     print(i[0],i[1],end=" ")
    # print()
    # return new_data

string=input()

N_freq=int(input())

# N_vals=input().split()
N_vals= list(map(int, input().split()))
#new_data=freq(string)
data={}
for ch in string:
    if ch in data:
        data[ch]+=1
    else:
        data[ch]=1
new_data=list(data)
# print(type(data[new_data[1]]))
print1(new_data,data)
for j in range(N_freq):
    N=int(N_vals[j])
    new_data = arrange(new_data,N)
    print1(new_data,data)
