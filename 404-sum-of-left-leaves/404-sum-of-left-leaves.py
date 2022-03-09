# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumLeft(root,flag):
            if not root:
                return 
            if flag and not root.right and not root.left:
                self.s+=root.val
            else:
                sumLeft(root.left,1)
                sumLeft(root.right,0)
        sumLeft(root,0)
        return self.s