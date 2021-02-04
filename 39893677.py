# cook your dish here
def ende(a):
    a.append(a.pop(0))

n= int(input())
arr= list(map(int, input().split()))

def bc_kuchh_bhi(x, l):
    bc= True
    for i in l:
        if x<=i:
            bc= False
            return False
    if sorted(l)==l:
        return True
    return False

q=[arr[0]]
s=[]
print(arr[0])
i=1
while i< len(arr):
    if arr[i]>= q[-1]:
        q.append(arr[i])
    elif len(s)==0 or arr[i]<=s[-1]:
        s.append(arr[i])
    else:
        #1
        while len(s):
            if s[-1]< q[0]:
                q.append(s.pop())
            elif bc_kuchh_bhi(s[-1], q):
                q.append(s.pop())
            elif s[-1]==q[-1]:
                q.append(s.pop())
            else:
                ende(q)
        #2
        while q[0]<arr[i]:
            ende(q)
        
        #3
        s.append(q.pop(0))
        #4
        s.append(arr[i])
        #5
        while q[0]>=q[-1]:
            ende(q)
    
    if len(q):
        print(' '.join(map(str, q)))
    if len(s):
        print(' '.join(map(str, s[::-1])))
    i+=1
    