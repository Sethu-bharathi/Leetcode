this 
class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(' ')
        d={}
        l=[]
        for i in s:
            d[i[-1]]=i[:-1]
        for i in range(1,200):
            if str(i) in d:
                l.append(d[str(i)])
            else:
                break
        return ' '.join(l)
sentence=Solution()
s=input("enter the string")
print(sentence.sortSentence(s))
