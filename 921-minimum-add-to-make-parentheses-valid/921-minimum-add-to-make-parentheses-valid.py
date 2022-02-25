class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal=0
        count=0
        for i in s:
            if i=="(":
                bal+=1
            else:
                if not bal:
                    count+=1
                else:
                    bal-=1
        return count+bal