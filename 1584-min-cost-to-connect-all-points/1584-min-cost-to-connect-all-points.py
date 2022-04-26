class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        mst_cost=0
        edges=0
        
        in_mst=[0]*n
        
        min_dist=[math.inf]*n
        
        min_dist[0]=0
        
        while edges<n:
            curr_min_edge=math.inf
            curr_node=-1
            
            for node in range(n):
                if not in_mst[node] and curr_min_edge>min_dist[node]:
                    curr_min_edge=min_dist[node]
                    curr_node=node
                
            mst_cost+=curr_min_edge
            edges+=1
            in_mst[curr_node]=1
                
            for node in range(n):
                dist=abs(points[curr_node][0]-points[node][0])
                dist+=abs(points[curr_node][1]-points[node][1])
                if not in_mst[node] and min_dist[node] > dist:
                    min_dist[node]=dist
        return mst_cost