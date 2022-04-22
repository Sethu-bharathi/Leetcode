# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            self.res=max(l+r,self.res)
            return max(l,r)+1
        height(root)
        return self.res