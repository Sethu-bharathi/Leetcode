# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(1,root)]
        out = 0
        while q:
            n = len(q)
            for i in range(n):
                num, node = q.pop(0)
                if i == 0:
                    start = num
                if i == n-1:
                    end = num
                if node.left:
                    q.append((2*num,node.left))
                if node.right:
                    q.append((2*num+1,node.right))
            out = max(out,end-start+1)
        
        return out