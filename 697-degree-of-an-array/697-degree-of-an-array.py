class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d=collections.Counter(nums)
        maxi=0
        for i in d:
            maxi=max(d[i],maxi)
        left={}
        right={}
        for i in range(len(nums)):
            if d[nums[i]]==maxi:
                if nums[i] not in left:
                    left[nums[i]]=i
                right[nums[i]]=i
        count=len(nums)
        print(left,right)
        for i in left:
            if i in right:
                count=min(count,right[i]-left[i]+1)
        return count

            
        