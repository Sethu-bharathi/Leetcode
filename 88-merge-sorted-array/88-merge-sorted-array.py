class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first,second=m-1,n-1
        index=first+second+1
        while first>-1 and second>-1:
            if nums1[first]>nums2[second]:
                nums1[index]=nums1[first]
                first-=1
            else:
                nums1[index]=nums2[second]
                second-=1
        
            index-=1
        while first>-1:
            nums1[index]=nums1[first]
            first-=1
            index-=1
        while second>-1:
            nums1[index]=nums2[second]
            second-=1
            index-=1