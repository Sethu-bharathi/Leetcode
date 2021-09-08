class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]],i]
            else:
                d[nums[i]]=i
n=list(map(int,input().split()))
target=int(input())
Twosum=Solution()
print(Twosum.twoSum(n,target))