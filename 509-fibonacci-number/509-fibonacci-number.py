class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        first=0
        second=1
        for i in range(1,n):
            first,second=second,second+first
        return second
        