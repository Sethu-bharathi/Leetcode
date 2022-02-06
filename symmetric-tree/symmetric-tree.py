# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,left,right) -> bool:
        if not right and not left:
            return 1
        elif not left or not right:
            return 0
        if left.val!=right.val:
            return 0
        else:
            return self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1
        return self.isMirror(root.left,root.right)