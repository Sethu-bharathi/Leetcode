class Solution:
    def mergeAlternately(self, str1: str, str2: str) -> str:
        i,j=0,0
        res=""
        while i<len(str1) and j<len(str2):
            res+=str1[i]+str2[j]
            i+=1
            j+=1
        while i<len(str1):
            res+=str1[i]
            i+=1
        while j<len(str2):
            res+=str2[j]
            j+=1
        return res