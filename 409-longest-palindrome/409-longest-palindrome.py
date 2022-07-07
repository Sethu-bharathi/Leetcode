class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=Counter(s)
        count=0
        for i in d:
            num=d[i]
            count+=(num>>1)<<1
            if num&1 and not count&1:
                count+=1
        return count