a=[1,2,3,4,5,6]
if 3 in a:
    x=a.pop(a.index(3))
    print(x)
    a.append(x)
    print(a)