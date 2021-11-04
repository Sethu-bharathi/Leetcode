class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=str(x)
        if x>=0 and int(res[::-1])==x:
            return True
        return False