class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=nums[0]
        for i in range (1,len(nums)):
            n^=nums[i]
        return n
one=Solution()
nums=list(map(int,input().split()))
print(one.singleNumber(nums))