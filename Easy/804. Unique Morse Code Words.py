class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        count=0
        for i in words:
            s=""
            for j in i:
                s+=(code[ord(j)-ord("a")])
            if s not in d:
                count+=1
                d[s]=1
        return len(d)