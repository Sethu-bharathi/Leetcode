class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset=set()
        need=1<<k
        for i in range(k,len(s)+1):
            temp=s[i-k:i]
            if temp not in hashset:
                hashset.add(temp)
                need-=1
                if not need:
                    return 1
        return 0
                
            