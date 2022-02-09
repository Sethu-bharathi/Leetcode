class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        for i in d:
            if k>0 and i-k in d:
                count+=1
            elif k==0 and d[i]>1:
                count+=1
        return count
                