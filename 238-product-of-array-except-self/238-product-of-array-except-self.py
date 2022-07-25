class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left,right=1,1
        res=[1]*n
        for i in range(n):
            res[i]*=left
            res[-(i+1)]*=right
            left*=nums[i]
            right*=nums[-(i+1)]
        return res