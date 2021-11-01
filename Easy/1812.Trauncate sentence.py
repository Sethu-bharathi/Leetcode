class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=""
        index=0
        while index<len(s):
            if s[index]==" ":
                k-=1
            if k==0:
                return res
            res+=s[index]
            index+=1
        return res
        