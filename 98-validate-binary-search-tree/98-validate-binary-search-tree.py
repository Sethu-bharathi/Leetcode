# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev=None 
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1
        if not self.isValidBST(root.left):
            return 0
        if self.prev and self.prev.val>=root.val:
            return 0
        self.prev=root
        return self.isValidBST(root.right)
            
        