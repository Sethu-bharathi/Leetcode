class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j=0,0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        