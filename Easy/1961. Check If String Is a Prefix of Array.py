class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i=0
        res=""
        while i<len(words):
            res+=words[i]
            i+=1
            if len(s)<len(res):
                return 0
            if res==s:
                return 1
        return 0
            