class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i=="(":
                stack.append(i)
            else:
                if not stack:
                    count+=1
                else:
                    stack.pop()
        return count+len(stack)