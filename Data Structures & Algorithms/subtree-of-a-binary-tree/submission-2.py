class Solution:
    def compare(self, a, b):
        if not a and not b:
            return True
        
        if (not a and b) or (a and not b):
            return False

        if a.val != b.val:
            return False

        return self.compare(a.left, b.left) and self.compare(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.compare(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)