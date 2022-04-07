class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums=[]
        for i in stones:
            heapq.heappush(nums,-i)
        while len(nums)>1:
            temp1=heapq.heappop(nums)
            temp2=heapq.heappop(nums)
            heapq.heappush(nums,-abs(temp1-temp2))
        if nums:
            return -nums[0]
        return 0