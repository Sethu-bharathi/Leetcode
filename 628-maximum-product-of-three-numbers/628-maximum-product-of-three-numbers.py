class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        third,second,first=-float("inf"),-float("inf"),-float("inf")
        min1,min2=float("inf"),float("inf")
        for i in range(len(nums)):
            if nums[i]>=third:
                third,second,first=nums[i],third,second
            elif nums[i]>=second:
                second,first=nums[i],second
            elif nums[i]>=first:
                first=nums[i]
            if nums[i]<=min1:
                min1,min2=nums[i],min1
            elif nums[i]<=min2:
                min2=nums[i]
        
        return max(third*second*first,min1*min2*third)
            
        