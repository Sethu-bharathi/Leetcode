class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        d={}
        i=0
        res=0
        for j in range(len(s)):
            if s[j] in d:
                i=max(i,d[s[j]]+1)
            maxend=j-i+1
            res=max(res,maxend)
            d[s[j]]=j
        return res
                
                
        