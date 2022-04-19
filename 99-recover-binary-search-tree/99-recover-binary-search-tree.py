# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first,self.prev,self.second=None,None,None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev and not self.first and self.prev.val>root.val:
                self.first=self.prev
            if self.first and self.prev.val>root.val:
                self.second=root
            self.prev=root
            inorder(root.right)
        
        inorder(root)
        self.first.val,self.second.val=self.second.val,self.first.val
    
            
        