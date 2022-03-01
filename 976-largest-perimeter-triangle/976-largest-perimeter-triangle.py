class Solution:
    def isTriangle(self,a,b,c):
        return a+b>c and b+c>a and a+c>b
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter=0
        for i in range(len(nums)-1,1,-1):
            if self.isTriangle(nums[i],nums[i-1],nums[i-2]):
                perimeter=max(perimeter,nums[i-2]+nums[i-1]+nums[i])
        return perimeter
        
        