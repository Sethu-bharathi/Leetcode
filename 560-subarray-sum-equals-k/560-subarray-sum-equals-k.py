class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        d={0:1}
        sum=0
        for i in nums:
            sum+=i
            if sum-k in d:
                count+=d[sum-k]
            if sum in d:
                d[sum]+=1
            else:
                d[sum]=1
        return count
                
                
                