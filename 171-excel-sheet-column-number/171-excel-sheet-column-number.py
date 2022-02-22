class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count=0
        for i in columnTitle:
            count=count*26+ord(i)-ord("A")+1
        return count