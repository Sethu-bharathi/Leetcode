class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def cansplit(n)->bool:
            subarray=1
            curr=0
            for i in nums:
                curr+=i
                if curr>n:
                    curr=i
                    subarray+=1
            return subarray<=m
        
        l,r=max(nums),sum(nums)
        while l<=r:
            mid=l-(l-r)//2
            if cansplit(mid):
                res= mid
                r=mid-1
            else:
                l=mid+1
        return res