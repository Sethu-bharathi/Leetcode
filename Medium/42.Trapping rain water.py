class Solution:
    def trap(self, height: List[int]) -> int:
        lax=0
        lmax=[0 for i in height]
        rmax=[0 for i in height]
        for i in range(len(height)):
            if height[i]>lax:
                lax=height[i]
            lmax[i]=lax
        lax=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>lax:
                lax=height[i]
            rmax[i]=lax
        count=0
        for i in range(1,len(height)-1):
            count+=min(rmax[i],lmax[i])-height[i]
        return count
        