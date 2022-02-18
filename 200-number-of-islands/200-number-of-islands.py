class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C=len(grid),len(grid[0])
        count=0
        def dfs(l,r):
            if grid[l][r]=="1":
                grid[l][r]="0"
                if l>=1:dfs(l-1,r)
                if l+1<R:dfs(l+1,r)
                if r>=1:dfs(l,r-1)
                if r+1<C:dfs(l,r+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count