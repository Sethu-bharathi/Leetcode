class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words=sorted(words,key=len)
        dp={}
        count=0
        for i in words:
            dp[i]=max([dp.get(i[:k]+i[k+1:],0)+1 for k in range(len(i))])
            count=max(count,dp[i])
        return count