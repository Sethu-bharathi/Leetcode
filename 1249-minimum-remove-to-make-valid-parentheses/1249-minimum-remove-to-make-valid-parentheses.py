class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        d={}
        res=""
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if len(stack):
                    stack.pop()
                else:
                    d[i]=1
        for i in stack:
            d[i]=1
        for i in range(len(s)):
            if i not in d:
                res+=s[i]
        return res