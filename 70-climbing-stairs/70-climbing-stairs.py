
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=2):
            return n
        else:
            a = [0 for i in range(n+1)]
            a[1] = 1
            a[2] = 2
            for i in range(3,n+1):
                a[i]=a[i-1]+a[i-2]
            return a[n]

