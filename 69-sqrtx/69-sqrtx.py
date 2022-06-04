class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        start=2
        end=x>>1
        while start<=end:
            mid=(start)-((start-end)//2)
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                end=mid-1
            else:
                start=mid+1
        return end
            
        