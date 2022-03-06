class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums=sorted(list(set(nums)))
        sum=(k*(k+1))>>1
        for i in nums:
            if i<=k:
                k+=1
                sum+=k-i
            else:
                break
        return sum
            
                