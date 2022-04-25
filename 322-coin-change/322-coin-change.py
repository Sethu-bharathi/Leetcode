class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf") for i in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            temp=float("inf")
            for j in coins:
                if i-j>=0:
                    temp=min(dp[i-j],temp)
            if temp!=float("inf"):
                dp[i]=temp+1
        if dp[-1]==float("inf"):
            return -1
        return dp[-1]