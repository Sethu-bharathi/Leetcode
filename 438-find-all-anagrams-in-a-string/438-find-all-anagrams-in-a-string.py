class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map={}
        s_map={}
        res=[]
        if len(s)<len(p):
            return []
        for i in p:
            if i in p_map:
                p_map[i]+=1
            else:
                p_map[i]=1
        for i in range(len(p)):
            if s[i] in s_map:
                s_map[s[i]]+=1
            else:
                s_map[s[i]]=1
        if s_map==p_map:
            res.append(0)
        for i in range(len(p),len(s)):
            if s[i] in s_map:
                s_map[s[i]]+=1
            else:
                s_map[s[i]]=1
            if s_map[s[i-len(p)]]==1:
                del(s_map[s[i-len(p)]])
            else:
                s_map[s[i-len(p)]]-=1
            if p_map==s_map:
                res.append(i-len(p)+1)
        return res