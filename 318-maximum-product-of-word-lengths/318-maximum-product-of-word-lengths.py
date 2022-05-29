class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d={}
        for i in words:
            count=0
            for j in set(i):
                count|=1<<ord(j)-96
            d[count]=max(d.get(count,0),len(i))
        return max([d[x]*d[y] for x in d for y in d if not x&y] or [0])
        
                