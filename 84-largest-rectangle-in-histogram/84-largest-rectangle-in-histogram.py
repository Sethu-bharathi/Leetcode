class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[0]
        n=len(heights)
        res=0
        for i in range(1,n):
            while stack and heights[stack[-1]]>=heights[i]:
                curr=stack.pop()
                res=max(res,heights[curr]*(i if not stack else i-stack[-1]-1))
            stack.append(i)
        while stack:
            curr=stack.pop()
            res=max(res,heights[curr]*(n if not stack else n-stack[-1]-1))
        return res
                
                