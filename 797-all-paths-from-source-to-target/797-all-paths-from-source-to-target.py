class Solution:
    def __init__(self):
        self.res=[]
    def paths(self,graph,target,index,res):
        if index==target:
            self.res.append(res)
            return 
        for i in graph[index]:
            self.paths(graph,target,i,res+[i])
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target=len(graph)-1
        n=target+1
        self.paths(graph,target,0,[0])
        return self.res