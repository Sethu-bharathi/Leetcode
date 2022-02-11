class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        d1={}
        d2={}
        for i in range(n1):
            if s1[i] in d1:
                d1[s1[i]]+=1
            else:
                d1[s1[i]]=1
            if s2[i] in d2:
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
        for i in range(n1,n2):
            if d1==d2:
                return 1
            if s2[i] in d2:
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
            if d2[s2[i-n1]]==1:
                del d2[s2[i-n1]]
            else:
                d2[s2[i-n1]]-=1
        return d1==d2
            