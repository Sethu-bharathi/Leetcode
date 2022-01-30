class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=1
        first=1
        while first in d:
            first+=1
        return first