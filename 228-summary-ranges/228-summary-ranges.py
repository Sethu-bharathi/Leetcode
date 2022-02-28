class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        last=nums[0]
        res=[]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if last!=nums[i-1]:
                    res.append(str(last)+"->"+str(nums[i-1]))
                else:
                    res.append(str(last))
                last=nums[i]
        if last==nums[-1]:
            res.append(str(last))
        else:
            res.append(str(last)+"->"+str(nums[-1]))
        return res
                
            