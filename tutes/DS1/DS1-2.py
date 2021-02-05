my_list=["hello","world","345","my","name","123","is","my","aa","jagrit","123","aa","jagrit","hello","aaa","my",]
my_list.sort()
pos=0
lenght=len(my_list)
while True:
	if pos>=lenght-1:
		break
	elif my_list[pos]==my_list[pos+1]:
		my_list.remove(my_list[pos])
		lenght=lenght-1
		continue
	else:
		pos=pos+1
print(my_list)