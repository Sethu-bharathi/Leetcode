class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)-1,-1,-1):
            k+=nums[i]
            nums[i]=k%10
            k//=10
        while k:
            nums=[k%10]+nums
            k//=10
        return  nums