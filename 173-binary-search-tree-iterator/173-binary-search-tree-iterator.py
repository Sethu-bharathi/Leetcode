# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.stack=[]
        self.add(root)

    def next(self) -> int:
        curr=self.stack.pop()
        self.add(curr.right)
        return curr.val
        
    def add(self,root):
        while root:
            self.stack.append(root)
            root=root.left

    def hasNext(self) -> bool:
        return len(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()