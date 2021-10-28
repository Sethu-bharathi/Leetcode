class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        if n<0:
            if n%2==1:
                return (1/x)*self.myPow(x,n+1)
            else:
                temp=self.myPow(x,n//2)
                return temp*temp
        if n%2==0:
            temp=self.myPow(x,n//2)
            return temp*temp
        if n%2==1:
            return x*self.myPow(x,n-1)