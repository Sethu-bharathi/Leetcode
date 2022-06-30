class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median=nums[len(nums)>>1]
        count=0
        for i in range(len(nums)):
            count+=abs(nums[i]-median)
        return count