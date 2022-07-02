class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max1,max2=horizontalCuts[0],verticalCuts[0]
        for i in range(len(horizontalCuts)-1):
            max1=max(max1,horizontalCuts[i+1]-horizontalCuts[i])
        
        max1=max(max1,-horizontalCuts[-1]+h)
        
        for i in range(len(verticalCuts)-1):
            max2=max(max2,verticalCuts[i+1]-verticalCuts[i])
        max2=max(max2,-verticalCuts[-1]+w)
        return (max1*max2)%(10**9+7)