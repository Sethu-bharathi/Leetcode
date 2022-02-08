class Solution:
    def __init__(self):
        self.arr=[]
    def twosum(self, index : int, target : int, nums : List[int]):
        left=index+1
        right=len(nums)-1
        while left<right:
            s=target+nums[left]+nums[right]
            if s==0:
                self.arr.append([nums[index],nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and (nums[left]==nums[left-1]):
                    left+=1
            elif s<0:
                left+=1
            else:
                right-=1
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        self.twosum(0,nums[0],nums)
        for i in range(1,len(nums)-2):
            if nums[i]!=nums[i-1]:
                print("looping",i)
                self.twosum(i,nums[i],nums)
        return self.arr
        
        