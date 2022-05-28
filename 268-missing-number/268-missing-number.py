class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        # return ((l*(l+1))//2-sum(nums))
        sum=0
        for i in range(l):
            sum^=nums[i]^i
        sum^=l
        return sum
        