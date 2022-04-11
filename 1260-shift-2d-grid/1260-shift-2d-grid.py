class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        k%=m*n
        for _ in range(k):
            temp=grid[-1][-1]
            for i in range(m):
                for j in range(n):
                    grid[i][j],temp=temp,grid[i][j]
        return grid