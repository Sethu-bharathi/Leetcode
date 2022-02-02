class Solution:
    def jump(self,nums:List[int],x:int)->bool:
        if x==0:
            return 1
        for i in range(x):
            if nums[i]+i>=x and self.jump(nums,i):
                    return 1
        return 0
        
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=last:last=i
        if last==0:
            return 1
        return 0
                