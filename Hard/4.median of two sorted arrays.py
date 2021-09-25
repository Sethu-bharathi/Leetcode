class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1=sorted(nums1)
        n=len(nums1)
        if n%2==0:
            n=n//2
            return (nums1[n]+nums1[n-1])/2
        n=n//2
        return nums1[n]
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
median=Solution()
print(median.findMedianSortedArrays(nums1,nums2))