class Solution:
    import heapq
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        n=len(arr)
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        arr=[i*-1 for i in list(d.values())]
        heapq.heapify(arr)
        count=0
        re=0
        while count<n//2:
            count-=heapq.heappop(arr)
            re+=1
        return re
        
        
        
        