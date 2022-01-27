class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        right=1
        res=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            res[i]*=left
            res[-(1+i)]*=right
            left*=nums[i]
            right*=nums[-(i+1)]
        return res
            
        