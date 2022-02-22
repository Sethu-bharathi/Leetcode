class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        d=[0 for i in range(n+1)]
        out=[0 for i in range(n+1)]
        for i in trust:
            d[i[1]]+=1
            out[i[0]]+=1
        for i in range(1,n+1):
            if out[i]==0 and d[i]==n-1:
                return i
        return -1
            