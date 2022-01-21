class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        i,j=0,len(nums)-1
        while j>i:
            if k==(nums[i]+nums[j]):
                return [i+1,j+1]
            if (nums[i]+nums[j])>k:
                j -= 1
            else:
                i += 1