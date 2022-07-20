class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word=collections.defaultdict(list)
        for i in words:
            word[i[0]].append(i)
        count=0
        for i in s:
            temp=word[i]
            word[i]=[]
            for j in temp:
                if len(j)==1:
                    count+=1
                else:
                    word[j[1]].append(j[1:])
        return count
                    