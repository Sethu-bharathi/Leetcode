class Solution:
    def countHillValley(self, num: List[int]) -> int:
        res=0
        nums=[]
        for i in range(0,len(num)-1):
            if num[i]!=num[i+1]:
                nums.append(num[i])
        if not nums or nums[-1]!=num[-1]:
            nums.append(num[-1])
        for i in range(1,len(nums)-1):
            if (nums[i]>nums[i-1] and nums[i]>nums[i+1])or(nums[i]<nums[i-1] and nums[i]<nums[i+1]):
                res+=1
        return res
                