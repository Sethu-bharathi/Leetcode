class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even,odd=0,len(nums)-1
        while even<odd:
            if nums[odd]%2==0 and nums[even]%2==1:
                nums[even],nums[odd]=nums[odd],nums[even]
            if nums[odd]%2:
                odd-=1
            if nums[even]%2==0:
                even+=1
        return nums