class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if len(nums)==1:
            return 0
        
        while l<r:
            mid=(r+l)>>1
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l
            
            