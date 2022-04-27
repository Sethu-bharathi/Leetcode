class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        l=len(s)
        visited=[0]*l
        adj=[[] for i in range(l)]
        for i in pairs:
            x,y=i
            adj[x].append(y)
            adj[y].append(x)
        s=[i for i in s]
        
        def dfs(s,vertex,character,index):
            
            visited[vertex]=1
            character.append(s[vertex])
            index.append(vertex)
            
            for  i in adj[vertex]:
                if not visited[i]:
                    dfs(s,i,character,index)
                    
        for vertex in range(l):
            if not visited[vertex]:
                character=[]
                index=[]
                dfs(s,vertex,character,index)
                
                character.sort()
                index.sort()
                
                for i in range(len(index)):
                    s[index[i]]=character[i]
        return "".join(s)