# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root,maxval)->int:
            if not root:
                return 0
            if root.val>=maxval:
                return 1+traverse(root.left,root.val)+traverse(root.right,root.val)
            return traverse(root.left,maxval)+traverse(root.right,maxval)
        return traverse(root,root.val)