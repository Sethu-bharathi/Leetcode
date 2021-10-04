class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def findDepth(self,root,count):
            if(not root):
                return 0
            elif(not root.left and not root.right):
                return count+1
            return min(findDepth(root.left,count+1),findDepth(root.right,count+1))
        return findDepth(root,0)