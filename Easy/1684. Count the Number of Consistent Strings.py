class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d={}
        count=0
        for i in allowed:
            d[i]=1
        for i in words:
            flag=1
            for j  in i:
                if j not in d:
                    flag=0
                    break
            if flag:
                count+=1
        return count