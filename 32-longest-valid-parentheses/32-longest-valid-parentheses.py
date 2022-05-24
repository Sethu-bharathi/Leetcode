class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        count=0
        fn=len
        stack.append(-1)
        for i in range(fn(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if fn(stack)==0:
                    stack.append(i)
                else:
                    count=max(count,i-stack[-1])
        return count
                    
        