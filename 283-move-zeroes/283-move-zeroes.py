class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if(len(nums)==1):
            return nums
        index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0
        return nums