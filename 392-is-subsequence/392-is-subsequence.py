class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        index=0
        for i in range(len(t)):
            if t[i]==s[index]:
                index+=1
            if index==len(s):
                return True
        return False
            
            
        