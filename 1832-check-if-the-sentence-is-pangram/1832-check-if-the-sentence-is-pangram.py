class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d=collections.Counter(sentence)
        return len(d)==26