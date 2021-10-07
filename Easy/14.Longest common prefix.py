class Solution:
    def longestCommonPrefix(self, s: list[str]) -> str:
        if len(s)==0:
            return None
        def longprefix(s,left,right):
            if left==right:
                return s[right]
            mid=(left+right)>>1
            s1=longprefix(s,left,mid)
            s2=longprefix(s,mid+1,right)
            l=min(len(s1),len(s2))
            for i in range(l):
                if s1[i]!=s2[i]:
                    return s1[:i]
            return s1[:l]
        return longprefix(s,0,len(s)-1)
                
Prefix=Solution()
s=input().split()
print(Prefix.longestCommonPrefix(s))