class Solution:
    def decodeString(self, s: str) -> str:
        stack=[""]
        num=0
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            elif s[i]=="[":
                stack.append(num)
                num=0
                stack.append("")
            elif s[i]=="]":
                first=stack.pop()
                n=stack.pop()
                last=stack.pop()
                stack.append(last+n*first)
            else:
                stack[-1]+=s[i]
        return "".join(stack)
            
                