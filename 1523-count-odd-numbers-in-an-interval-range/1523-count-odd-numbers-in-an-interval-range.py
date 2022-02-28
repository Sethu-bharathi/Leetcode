class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        if low%2 or high%2:
            count+=1
        count+=(high-low)>>1
        return count