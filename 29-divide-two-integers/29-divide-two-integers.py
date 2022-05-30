class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a,b=abs(dividend),abs(divisor)
        a//=b
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            if a>2**31:
                return -2**31
            return -a
        if a>=2**31:
            return (2**31)-1
        return a
            
            
        