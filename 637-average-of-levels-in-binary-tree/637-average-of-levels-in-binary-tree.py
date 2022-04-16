# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=[root]
        while queue:
            count=0
            l=len(queue)
            for i in range(l):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                count+=curr.val
            self.res.append(count/l)
        return self.res
        
        
        