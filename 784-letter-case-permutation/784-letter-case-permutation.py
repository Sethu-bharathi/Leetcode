class Solution:
    def __init__(self):
        self.res=[]
    def permutations(self,s,index,string1):
        if index==len(s):
            self.res.append(string1)
            return 0
        if s[index].isalpha():
            self.permutations(s,index+1,string1+s[index].upper())
            self.permutations(s,index+1,string1+s[index].lower())
        else:
            self.permutations(s,index+1,string1+s[index])
    
    def letterCasePermutation(self, s: str) -> List[str]:
        self.permutations(s,0,"")
        return (self.res)
    
        
            
        