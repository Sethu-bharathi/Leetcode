class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res=0
        while startValue<target:
            res+=1
            if target%2:
                target+=1
            else:
                target//=2
        if target==startValue:
            return res
        return res+(startValue-target)
            