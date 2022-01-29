class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[0]
        for j in range(len(nums)):
            i=nums[j]
            res[0]^=abs(i)
            res[0]^=j+1
            if nums[abs(i)-1]<0:
                res.append(abs(i))
            else:
                nums[abs(i)-1]*=-1
        res[0]^=res[1]
        return res[::-1]
        