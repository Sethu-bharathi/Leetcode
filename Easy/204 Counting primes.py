
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        primes=[True for i in range(n)]
        x=2
        primes[0]=primes[1]=False
        while x**2<=n:
            if primes[x]:
                for i in range(x*x,n,x):
                    primes[i]=False
            x+=1
        return primes.count(True)

n=int(input("Enter the number"))
prime1=Solution()
print(prime1.countPrimes(n))