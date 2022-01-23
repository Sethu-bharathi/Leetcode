class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        d={}
        for i in range (n):
            if s[i] in d:
                d[s[i]]=-1
            else:
                d[s[i]]=i
        for i in d:
            if d[i]!=-1:
                return d[i]
        return -1
            