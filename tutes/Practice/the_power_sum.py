import math
def powerSum(x,n,cNum=1,cSum=0):
    result=0
    while cSum+cNum**n<x:
        result+=powerSum(x,n,cNum+1,cNum**n+cSum)
        cNum+=1
    if cSum+cNum**n==x:
        return result+1
    return result


if __name__ == '__main__':
    X = int(input("x"))
    N = int(input("n"))
    result = powerSum(X, N)
    print(result)

#1 0
    #2 1
        #3 5 none
    #3 1
        #4 10 none
    #4 1 none
#2 0
    #3 4 none
#3 0
    #4 9 none