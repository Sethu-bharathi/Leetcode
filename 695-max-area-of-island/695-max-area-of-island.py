class Solution:
    def __init__(self):
        self.maxarea=0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=0
        R,C=len(grid),len(grid[0])
        
        def dfs(r,c):
            count=0
            if grid[r][c]==1:
                count+=1
                grid[r][c]=0
                if r>=1:
                    count+=dfs(r-1,c)
                if r+1<R:
                    count+=dfs(r+1,c)
                if c>=1:
                    count+=dfs(r,c-1)
                if c+1<C:
                    count+=dfs(r,c+1)
                
            return count
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    maxarea=max(maxarea,dfs(i,j))
        return maxarea