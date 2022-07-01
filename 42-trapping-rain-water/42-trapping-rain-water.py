class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        lmax,rmax=[0]*l,[0]*l
        maxele=0
        for i in range(l):
            maxele=max(maxele,height[i])
            lmax[i]=maxele
        maxele=0
        for i in range(l-1,-1,-1):
            maxele=max(maxele,height[i])
            rmax[i]=maxele
        
        count=0
        for i in range(l):
            count+=min(lmax[i],rmax[i])-height[i]
        return count
            
        