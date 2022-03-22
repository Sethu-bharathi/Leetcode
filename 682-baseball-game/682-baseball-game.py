class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        if not ops:
            return 0
        for i in ops:
            if i=="+":
                stack.append(stack[-1]+stack[-2])
            elif i=="C":
                stack.pop()
            elif i=="D":
                stack.append(stack[-1]<<1)
            else:
                stack.append(int(i))
                
        return sum(stack)