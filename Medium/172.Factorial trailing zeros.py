class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        i=5
        while i<=n:
            count+=n//i
            i*=5
        return count
zeros=Solution()
n=int(input())
print(zeros.trailingZeroes(n))