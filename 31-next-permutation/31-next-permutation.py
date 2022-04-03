class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l=len(nums)-2
        
        def swap(x,y):
            while x<y:
                nums[x],nums[y]=nums[y],nums[x]
                x+=1
                y-=1
                
        while l>=0 and nums[l+1]<=nums[l]:
            l-=1
        
        if l<0:
            swap(l+1,len(nums)-1)
            return
        i=len(nums)-1
        while nums[i]<=nums[l]:
            i-=1
        nums[i],nums[l]=nums[l],nums[i]
        swap(l+1,len(nums)-1)
        
        