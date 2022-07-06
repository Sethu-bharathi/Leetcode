class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        selling_price=prices[-1]
        profit=0
        for i in range(len(prices)-2,-1,-1):
            selling_price=max(selling_price,prices[i])
            profit=max(profit,selling_price-prices[i])
        return profit
            
            
                
            
            