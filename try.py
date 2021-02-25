#User function Template for python3
# design the class in the most optimal way
from collections import defaultdict
class LRUCache:
    def __init__(self,cap):
        # cap:  capacity of cache
        #Intialize all variable
        #code here
        self.cap=cap
        print(cap)
        self.dic=defaultdict(lambda: int(-1))
        self.Q=[]
    #This method works in O(1)
    def get(self, key):
        print("\n","        get ",key,end=" ")
        return (self.dic[key])

    #This method works in O(1)   
    def set(self, key, value):
        if len(self.Q)<cap and len(self.Q)>=0:
            self.Q.append(key)
            self.dic[key]=value
        elif(key in self.Q):
            q=self.Q
            self.dic[key]=value
            x=q.pop(q.index(key))
            q.append(x)
        else:
            x=self.Q.pop(0)
            self.dic[key]=value
            self.dic[x]=-1
            self.Q.append(key)
            
            
        print("\nset ",key,value,end=" ")
#{ 

#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = 1
    for cases in range(1):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        lru=LRUCache(cap)
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends

