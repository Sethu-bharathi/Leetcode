class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        d={}
        count=0
        res=0
        for i in range(3):
            if s[i] in d and d[s[i]]!=0:
                d[s[i]]+=1
            else:
                count+=1
                d[s[i]]=1
        for i in range(3,len(s)):
            print(d,count)
            if count==3:
                res+=1
            if s[i] in d and d[s[i]]!=0:
                d[s[i]]+=1
            else:
                d[s[i]]=1
                count+=1
            d[s[i-3]]-=1
            if d[s[i-3]]==0:
                count-=1
        if count==3:
            res+=1
        return res
                  
                