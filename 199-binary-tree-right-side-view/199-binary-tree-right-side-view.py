# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.right(root,[])
    def right(self,root,arr):
        if root is None:
            return arr
        res=[]
        queue=[root]
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return res