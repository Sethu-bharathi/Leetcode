# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d={}
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return 0
        
        if self.findTarget(root.left,k):
            return 1
        if k-root.val in self.d:
            return 1
        self.d[root.val]=1
        return self.findTarget(root.right,k)
            
        