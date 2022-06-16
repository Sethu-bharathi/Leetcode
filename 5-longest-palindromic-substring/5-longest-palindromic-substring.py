class Solution:
    def longestPalindrome(self, s: str) -> str:
        dist=""
        if len(s)==1:
            return s
        elif len(s)==2:
            if s[0]==s[1]:
                return s
            return s[0]
            
        n=len(s)
        for i in range(0,len(s)):
            if s[i]==s[i-1]:
                l=i-1
                r=i
                while l>-1 and r<n and s[l]==s[r]:
                    r+=1
                    l-=1
                if len(dist)<len(s[l+1:r]):
                    dist=s[l+1:r]
            l=i
            r=i
            while l>-1 and r<n and s[l]==s[r]:
                r+=1
                l-=1
            if len(dist)<len(s[l+1:r]):
                dist=s[l+1:r]
        return dist