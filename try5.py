class Solution:
    def numDecodings(self, s: str) -> int:
        tlen=len(s)
        if s[0]=='0':return 0
        def find(i):
            if s=="2617":
                print(i)
            if i==tlen:
                return 1
            r=0
            if  s[i]!='0':
                r+=find(i+1)
                if i<tlen-1:
                    print(i,tlen-1,int(s[i:i+2])<=26,int(s[i:i+2]))
                if i<tlen-1 and int(s[i:i+2])<=26:
                    r+=find(i+2)
            return r
        return find(0)

# o=[2,3,4]
                
# o={'A': 1, 'B': 0, 'C': 0}
# print(0<=(o))




s="2617".rstrip()
k=Solution().numDecodings(s)
print(k)
