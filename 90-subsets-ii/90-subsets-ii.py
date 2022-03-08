class Solution:
    def __init__(self):
        self.res=[]
    def dfs(self,nums,arr):
        self.res.append(arr)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.dfs(nums[i+1:],arr+[nums[i]])
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs(nums,[])
        return (self.res)