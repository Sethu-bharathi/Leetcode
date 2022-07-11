"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res=[]
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            self.res.append(root.val)
            for i in root.children:
                self.preorder(i)
        return self.res
            