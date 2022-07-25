class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        res=0
        a,b=1,1
        while b<=k                                                            :
            a,b=b,a+b
        while k:
            if k>=a:
                k-=a
                res+=1
            a,b=b-a,a
        return res
        