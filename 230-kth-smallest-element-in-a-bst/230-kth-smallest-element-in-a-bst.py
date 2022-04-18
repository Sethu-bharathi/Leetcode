# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
        self.res=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root and self.count<k:
                inorder(root.left)
                self.count+=1
                if self.count==k:
                    self.res=root.val
                    return
                inorder(root.right)
        inorder(root)
        return self.res
            