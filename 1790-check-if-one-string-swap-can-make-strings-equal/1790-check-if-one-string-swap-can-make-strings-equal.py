class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first,second=0,0
        flag=0
        diff=0
        if set(s1)!=set(s2):
            return 0
        while first<len(s1):
            if s1[first]!=s2[second]:
                diff+=1
            
            first+=1
            second+=1
        return diff==0 or diff==2