from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return 1
        one=0
        two=round(sqrt(c))
        while one<=two:
            if one**2+two**2<c:
                one+=1
            elif one**2+two**2>c:
                two-=1
            else:
                return 1
        return 0
                    