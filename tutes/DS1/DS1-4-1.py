my_list=["hello","world","345","my","name","123","is","my","aa","jagrit","123","aa","jagrit","hello","aaa","my",]
length=len(my_list)
new_list=[]
for pos in range(length):
    new_list.append(my_list[length-pos-1])
print(new_list)