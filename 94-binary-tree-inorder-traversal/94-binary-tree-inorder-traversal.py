class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] +                  self.inorderTraversal(root.right)