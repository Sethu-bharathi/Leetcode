class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count=0
        d={}
        for i in sentence:
            if i not in d:
                count+=1
                d[i]=1
        return count==26