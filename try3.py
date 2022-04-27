class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo={}
        tlen=len(s)
        ans=""
        def convert(i,j):
            return str(i)+str(j)
        def isPal(i,j):
            ij=convert(i,j)
            if ij in memo:
                return memo[ij]
            if s[i]!=s[j]:
                return False
            if i==j:
                memo[ij]=True
                return True
            if j==i+1:
                memo[ij]=s[i]==s[j]
                return memo[ij]
            return (isPal(i+1,j-1))
        for i in range(1,tlen):
            for j in range(0,i):
                if isPal(j,i):
                    if i-j+1>len(ans):
                        ans=s[j:i+1]
        print(isPal(0,len(s)-1))
        return ans
a="abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
k=Solution()
k=k.longestPalindrome(a)

print(k)
