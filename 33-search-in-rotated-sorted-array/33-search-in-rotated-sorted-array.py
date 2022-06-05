class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            print(left,right)
            mid=left+((right-left)>>1)
            if nums[mid]==target: return mid
            elif nums[mid]>=nums[left]:
                if nums[mid]>target and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return -1
                
                    
                