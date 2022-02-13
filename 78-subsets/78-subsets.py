class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(2**len(nums)):
            for j in range(len(nums)):
                if i&(1<<j):
                    res[-1].append(nums[j])
            res.append([])
        return res
        
        