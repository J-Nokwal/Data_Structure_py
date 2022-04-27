# class Solution:
#     def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
#         m=len(matrix)
#         n=len(matrix[0])
#         ans=[[0]*n for _ in range(m)]
#         rdict={}
#         cdict={}
#         acc=[]
#         for i in range(m):
#             for j in range(n):
#                 acc.append((matrix[i][j],i,j))
#         acc.sort(key= lambda i:i[0])
#         rdict[acc[0][1]]=[1,acc[0][0]]
#         cdict[acc[0][2]]=[1,acc[0][0]]
#         ans[acc[0][1]][acc[0][2]]=1
#         for k in range(1,len(acc)):
#             v,i,j=acc[k]
#             rank=1
#             if i in rdict:
#                 temp=rdict[i]
#                 if temp[1]==v:
#                     rankr=temp[0]
#                 else:
#                     rankr=temp[0]+1
#             else:
#                 rankr=1
#             if j in cdict:
#                 temp=cdict[j]
#                 if temp[1]==v:
#                     rankc=temp[0]
#                 else:
#                     rankc=temp[0]+1
#             else:
#                 rankc=1
#             rank=max(rank,rankr,rankc)
#             cdict[j]=rdict[i]=[rank,v]
#             ans[i][j]=rank
#             while acc[k-1][0]==v:
#                 tv,ti,tj=acc[k-1]
#                 # if ti==i or tj==j:
#                 #     ans[ti][tj]=ans[i][j]
#                 rcheck=rdict[ti][0] if rdict[ti][1]==tv else 0
#                 ccheck=cdict[tj][0] if cdict[tj][1]==tv else 0
#                 ans[ti][tj]=max(ans[ti][tj],rcheck,ccheck)
#                 k-=1
#                 if k==0:
#                     break
#         return ans

from itertools import product
class DSU:
    def __init__(self, graph):
        self.p = {i:i for i in graph}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
    def groups(self):
        ans = defaultdict(list)
        for el in self.p.keys():
            ans[self.find(el)].append(el)
        return ans
from collections import defaultdict        
class Solution:
    def matrixRankTransform(self, M):
        n, m = len(M), len(M[0])
        rank = [0] * (m + n)
        d = defaultdict(list)
        
        for i, j in product(range(n), range(m)):
            d[M[i][j]].append([i, j])
        for a in sorted(d):
            graph = [i for i, j in d[a]] + [j + n for i, j in d[a]]
            dsu = DSU(graph)
            for i, j in d[a]: dsu.union(i, j + n)

            for group in dsu.groups().values():
                mx = max(rank[i] for i in group)
                for i in group: rank[i] = mx + 1
                    
            for i, j in d[a]: M[i][j] = rank[i]
            
        return M
k=Solution()
a=[ [20 ,-21,14],
    [-19, 4 ,19],
    [22 ,-47,24],
    [-19, 4 ,19]
]
# a=[[-23,20,-49,-30,-39,-28,-5,-14],[-19,4,-33,2,-47,28,43,-6],[-47,36,-49,6,17,-8,-21,-30],[-27,44,27,10,21,-8,3,14],[-19,12,-25,34,-27,-48,-37,14],[-47,40,23,46,-39,48,-41,18],[-27,-4,7,-10,9,36,43,2],[37,44,43,-38,29,-44,19,38]]

k=k.matrixRankTransform(a)
print(k)