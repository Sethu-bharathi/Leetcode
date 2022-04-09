class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=collections.Counter(nums)
        heap=[]
        for i in d:
            if len(heap)<k:
                heapq.heappush(heap,[d[i],i])
            elif heap[0][0]<d[i]:
                heapq.heappop(heap)
                heapq.heappush(heap,[d[i],i])
        return [i for j,i in heap[::-1]]
            
                