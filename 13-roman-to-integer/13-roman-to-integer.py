class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=d[s[0]]
        for i in range(1,len(s)):
            sum+=d[s[i]]
            if d[s[i]]>d[s[i-1]]:
                sum-=(d[s[i-1]])*2
        return sum