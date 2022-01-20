class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count=0
        minprice=prices[0]
        for i in prices:
            if i<minprice:
                minprice=i
            elif i-minprice>count:
                count=i-minprice
        return count