class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in nums1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        for i in nums2:
            if i in d and d[i]>0:
                d[i]=-1
                res.append(i)
        return res
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
intersect=Solution()
print(intersect.intersection(nums1,nums2))