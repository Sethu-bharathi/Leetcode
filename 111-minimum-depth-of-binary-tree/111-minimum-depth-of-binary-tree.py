# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root.right and not root.left:
                return 1
            if not root.right:
                return dfs(root.left)+1
            elif not root.left:
                return dfs(root.right)+1
            return min(dfs(root.left),dfs(root.right))+1
        if not root:
            return 0
        return dfs(root)
        