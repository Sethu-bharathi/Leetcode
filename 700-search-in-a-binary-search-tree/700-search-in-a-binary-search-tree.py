# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
                return root
        while root.val!=val:
            
            if val==root.val:
                return root
            if val<root.val:
                root=root.left
            else:
                root=root.right
            if root==None:
                return root
        return root
        