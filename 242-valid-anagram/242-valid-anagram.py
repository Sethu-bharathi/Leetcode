import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return 0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i in d:
                d[i]-=1
            else:
                return 0
        for i in d:
            if d[i]:
                 return 0
        return 1
            
        
        