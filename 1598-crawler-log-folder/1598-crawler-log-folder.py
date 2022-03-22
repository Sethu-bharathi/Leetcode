class Solution:
    def minOperations(self, logs: List[str]) -> int:
        if not logs:
            return 0
        depth=0
        for i in logs:
            if i=="../":
                if depth>0:
                    depth-=1
            elif i=="./":
                pass
            else:
                depth+=1
        if depth>-1:
            return depth
        return 0