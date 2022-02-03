class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit=prices[-1]
        profit=0
        for i in range(len(prices)-2,-1,-1):
            min_profit=max(min_profit,prices[i])
            profit=max(profit,min_profit-prices[i])
            
        return profit
            
            
            
                
            
            