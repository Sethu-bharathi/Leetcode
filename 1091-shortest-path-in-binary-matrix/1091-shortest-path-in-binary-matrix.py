class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        if grid[0][0] or grid[r-1][c-1]:
            return -1
        
        def isvalid(i,j):
            return r>i>=0 and c>j>=0
        def bfs():
            queue=[(0,0,1)]
            dpos=[(-1,-1),(-1,0),(1,-1),(1,0),(0,-1),(-1,1),(0,1),(1,1)]
            count=1
            while queue:
                i,j,dist=queue.pop(0)
                if i==r-1 and j==r-1:
                    return dist
                for k in range(len(dpos)):
                    x,y=dpos[k]
                    if isvalid(i+x,j+y) and grid[i+x][j+y]!=1:
                        grid[i+x][j+y]=1
                        queue.append((i+x,j+y,dist+1))
            return -1
        return bfs()
                        