class Solution:
    def tribonacci(self, n: int) -> int:
        t2=1
        t1=1
        t0=0
        if n<2:
            return n
        for i in range(2,n):
            t0,t1,t2=t1,t2,t1+t2+t0
        return t2
n=int(input())
fibo=Solution()
print(fibo.tribonacci(n))