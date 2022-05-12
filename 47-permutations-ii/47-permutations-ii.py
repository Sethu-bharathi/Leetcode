class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def permutations(arr,count):
            if len(arr)==len(nums):
                res.append(arr)
                return
            for i in count:
                if count[i]>0:
                    count[i]-=1
                    permutations(arr+[i],count)
                    count[i]+=1
        permutations([],Counter(nums))
        return res