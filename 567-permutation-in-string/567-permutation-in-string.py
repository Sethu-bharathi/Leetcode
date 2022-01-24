class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        chars1, chars2 = {}, {}
        for i in range(n1):
            chars1[s1[i]] = 1 if s1[i] not in chars1 else chars1[s1[i]] + 1
        for i in range(n2):
            chars2[s2[i]] = 1 if s2[i] not in chars2 else chars2[s2[i]] + 1
            if i >= n1:
                if chars2[s2[i - n1]] > 1:
                    chars2[s2[i - n1]] -= 1
                else:
                    del chars2[s2[i - n1]]
            if chars1 == chars2:
                return True
        return False
            
            