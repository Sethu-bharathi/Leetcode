class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num:
            count+=1
            if num%2:
                num-=1
            else:
                num//=2
        return count