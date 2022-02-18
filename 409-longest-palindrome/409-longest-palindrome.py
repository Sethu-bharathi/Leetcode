class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        for i in d:
            num=d[i]
            count+=(num//2)*2
            if count%2==0 and num%2:
                count+=1
        return count