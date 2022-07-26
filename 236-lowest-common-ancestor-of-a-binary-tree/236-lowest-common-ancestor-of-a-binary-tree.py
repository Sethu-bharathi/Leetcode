# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res=None
        def dfs(self,head):
            if not head:return 0
            mid=0
            if head==p or head==q:
                mid= 1
            left=dfs(self,head.left)
            right=dfs(self,head.right)
            if (left and right) or (mid and (left or right)):
                self.res=head
                return 0
            return left or right or mid
        dfs(self,root)
        return self.res