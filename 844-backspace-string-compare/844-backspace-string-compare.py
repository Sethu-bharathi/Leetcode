class Solution:
    def formatstr(self,s:str)->str:
        stack=[]
        flag=0
        for i in s:
            if i=="#" and flag:
                flag-=1
                del stack[-1]
            elif i!="#":
                flag+=1
                stack.append(i)
        return "".join(stack)
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.formatstr(s)==self.formatstr(t)
        