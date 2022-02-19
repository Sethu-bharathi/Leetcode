class Solution:
    def numSquares(self, n: int) -> int:
        dp=[5 for i in range(n+1)]
        dp[0]=0
        dp[1]=1
        j=1
        for i in range(1,n+1):
            j=1
            while i>=j*j:
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        return dp[n]
            