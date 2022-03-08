class Solution:
    def __init__(self):
        self.res=[]
    def combination(self,digits,index,d,string):
        if index==len(digits) :
            self.res.append(string)
            return
        for i in d[digits[index]]:
            self.combination(digits,index+1,d,string+i)
            
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.combination(digits,0,d,"")
        return(self.res)
            