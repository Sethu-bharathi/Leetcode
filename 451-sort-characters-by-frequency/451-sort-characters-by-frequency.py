class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        d={}
        nums=[]
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            heapq.heappush(nums,[-d[i],i])
        s=""
        while nums:
            curr=heapq.heappop(nums)
            s+=-curr[0]*curr[1]
        return s