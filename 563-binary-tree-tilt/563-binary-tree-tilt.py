# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            if root:
                left=postorder(root.left)
                right=postorder(root.right)
                self.count+=abs(left-right)
                return left+right+root.val
            return 0
        postorder(root)
        return self.count