class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            else:
                if len(stack)==0:
                    return 0
                p=stack.pop()
                if ((p=="[" and i=="]") or (p=="{" and i=="}") or (p=="(" and i==")")):
                    continue
                else:
                    return 0
        return len(stack)==0
                    
valid=Solution()
paranthesis=input()
print(valid.isValid(paranthesis))