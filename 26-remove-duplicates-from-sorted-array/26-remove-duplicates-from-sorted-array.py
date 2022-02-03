class Solution:
    def removeDuplicates(self, nums: List[int]):
        if len(nums)!=0:
            curr=1
            for pos in range(1,len(nums)):
                if nums[pos]!=nums[pos-1]:
                    nums[curr]=nums[pos]
                    curr+=1
            return curr
    
                
            
        