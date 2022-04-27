from collections import Counter 
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        mp=Counter(nums)
        for i in mp.values():
            # print(i[1])
            if i%2==1:
                return False
        return True

a=Solution()
b=[3,2,3,2,2,2]
c=(a.divideArray(b))
print(c)