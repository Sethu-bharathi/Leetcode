class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[nums[i] for i in range(k)]
        heapq.heapify(heap)
        for j in range(k,len(nums)):
            if heap[0]<nums[j]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[j])
        return heap[0]
        