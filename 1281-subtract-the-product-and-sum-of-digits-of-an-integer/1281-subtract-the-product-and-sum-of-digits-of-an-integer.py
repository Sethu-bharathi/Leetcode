class Solution:
    def subtractProductAndSum(self, num: int) -> int:
        product=1
        sum=0
        while num:
            product*=num%10
            sum+=num%10
            num//=10
        return product-sum