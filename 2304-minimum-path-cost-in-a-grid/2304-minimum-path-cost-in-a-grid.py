class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        r,l=len(grid),len(grid[0])
        dp=[[0]*l for i in range(r)]
        for i in range(l):
            dp[0][i]=grid[0][i]
        
        def getmin(x,y):
            val=float("inf")
            for i in range(l):
                val=min(val,dp[x-1][i]+grid[x][y]+moveCost[grid[x-1][i]][y])
            return val
        for i in range(1,r):
            for j in range(l):
                dp[i][j]=getmin(i,j)
        return min(dp[-1])