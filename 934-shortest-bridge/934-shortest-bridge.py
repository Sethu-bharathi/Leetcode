class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        visited=set()
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        
        def isinvalid(r,c):
            return r>=0 and r<R and c>=0 and c<C
        
        
        def dfs(i,j):
            if not isinvalid(i,j) or not grid[i][j] or (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in direction:
                dfs(i+x,j+y)
        
        def bfs():
            res,queue=0,list(visited)
            while queue:
                for i in range(len(queue)):
                    x,y=queue.pop(0)
                    for i,j in direction:
                        a,b=x+i,j+y
                        if not isinvalid(a,b) or (a,b) in visited:
                            continue
                        if grid[a][b]:
                            return res
                        queue.append([a,b])
                        visited.add((a,b))
                res+=1
                        
            
        flag=0
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
        