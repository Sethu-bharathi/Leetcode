class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        l=0
        r=len(nums)-1
        res=[]
        while l<=r:
            mid=l-(l-r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            elif mid==0 or nums[mid]!=nums[mid-1]:
                res.append(mid)
                break
            else:
                r=mid-1
        if not res:
            return [-1,-1]
        l=res[0]
        r=len(nums)-1
        n=len(nums)
        while l<=r:
            mid=l-(l-r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            elif mid==n-1 or nums[mid]!=nums[mid+1]:
                res.append(mid)
                break
            else:
                l=mid+1
        return res
        