from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1=Counter(nums1)
        nums3=[]
        for i in nums2:
            if nums1[i] and nums1[i]>0:
                nums3.append(i)
                nums1[i]-=1
        return nums3
nums1=list(map(int,input().split()))        
nums2=list(map(int,input().split()))
intersect1=Solution()   
print(intersect1.intersect(nums1,nums2))
        