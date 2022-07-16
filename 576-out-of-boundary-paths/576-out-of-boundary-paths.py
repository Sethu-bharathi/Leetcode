class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, x: int, y: int) -> int:
        mod=10**9+7
        dp=[[0 for _ in range(n)] for i in range(m)]
        dp[x][y]=1
        count=0
        for _ in range(maxMove):
            dp1=[[0 for _ in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    down=dp[i+1][j] if i+1<m else 0
                    top=dp[i-1][j] if i-1>=0 else 0
                    right=dp[i][j+1] if j+1<n else 0
                    left=dp[i][j-1] if j-1>=0 else 0
                    
                    dp1[i][j]+=(down+top)%mod+(right+left)%mod
                    
            count+=(sum(dp[0])+sum(dp[-1]))%mod
            for i in range(m):
                count=(count+dp[i][0]+dp[i][-1])%mod
            dp,dp1=dp1,dp
        return count
            
                    