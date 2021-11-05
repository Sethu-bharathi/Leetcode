class Solution:
    def arrangeCoins(self, n: int) -> int:
        k=int(pow(2*n,1/2))
        if k*(k+1)>2*n:
            return k-1
        return k