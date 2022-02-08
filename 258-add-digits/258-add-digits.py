class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        count=0
        while num>9:
            count+=num%10
            num//=10
        count+=num
        if count>=10:
            return self.addDigits(count)
        return count
        