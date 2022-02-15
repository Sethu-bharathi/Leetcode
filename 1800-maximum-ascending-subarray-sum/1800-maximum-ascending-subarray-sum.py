class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l,r=0,0
        count,maxcount=nums[0],0
        for r in range(1,len(nums)):
            if nums[r-1]<nums[r]:
                count+=nums[r]
            else:
                maxcount=max(maxcount,count)
                count=nums[r]
                
        return max(maxcount,count)