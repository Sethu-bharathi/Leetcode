class Solution:
    def isHappy(self, n: int) -> bool: 
        def endless(n, l):
            if n==81:
                return 0
            if n in l:
                return False
            if n == 1:
                return True
            l[n]=1
            running_sum = 0
            while n > 0:
                running_sum += pow(n%10,2)
                n = n // 10
            
            return endless(running_sum,l)
        return endless(n,{})
        
        