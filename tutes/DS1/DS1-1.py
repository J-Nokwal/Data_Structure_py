my_list=["hello","world","my","name","is","aa","jagrit"]
def create():
    x=my_list.append(input("Enter word: "))
def display():
    print(my_list)
def insert():
    x=input("Enter word: ")
    y=int(input("Enter postion word should be on(index starts from 0): "))
    new_list=[]
    for k in range(y):
        new_list.append(my_list[k])
    new_list.append(x)
    for k in range(len(my_list)-y):
        new_list.append(my_list[k+y])
    return new_list
def delete():
    x=input("Enter word (CASE SENSITIVE): ")
    if x in my_list:
        y=my_list.index(x)
        my_list.remove(x)
    else:
        print("Word Not Found")
    return my_list
    
def search():
    x=input("search word: ")
    if x in my_list:
        print("Yes",x,"is in list and is at index:",my_list.index(x))
while True :
    cmd=input("-------------------------------------------------\n--MENU--\n1.CREATE\n2.DISPLAY\n3.INSERT\n4.DELETE\n5.SEARCH\n6.EXIT\n-------------------------------------------------\n")
    if cmd=="1" or cmd=="CREATE":
        create()
        continue
    elif cmd=="2" or cmd=="DISPLAY":
        display()
        continue
    elif cmd=="3":
        x=insert()
        my_list=x
        continue
    elif cmd=="4":
        print(delete())
        continue
    elif cmd=="5":
        search()
        continue
    elif cmd=="6":
        break
    else:
        print("INVALID INPUT")
print(my_list)