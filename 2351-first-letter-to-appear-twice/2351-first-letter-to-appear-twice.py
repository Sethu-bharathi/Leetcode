class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d=set()
        for i in s:
            if i in d:
                return i
            else:
                d.add(i)
            