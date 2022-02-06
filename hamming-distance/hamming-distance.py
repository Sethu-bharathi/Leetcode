class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num=x^y
        result = 0
        while num:
            result+=1
            num=num&(num-1)
        return result