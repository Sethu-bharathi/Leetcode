class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        edges=[[] for i in range(n)]
        for i in connections:
            u,v=i
            edges[v].append(u)
            edges[u].append(v)
        visited=[0]*n
        count=0
        def bfs(edges,visited,u):
            queue=[u]
            while queue:
                curr=queue.pop(0)
                for i in edges[curr]:
                    if visited[i]==0:
                        queue.append(i)
                        visited[i]=1
                        
        for i in range(n):
            if visited[i]==0:
                visited[i]=1
                bfs(edges,visited,i)
                count+=1
        return count-1
                
        
                    
            
            