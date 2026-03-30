# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def walkthr(self, node, depth):
        if not node:
            return depth

        return max(self.walkthr(node.left, depth+1), self.walkthr(node.right, depth+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs or dfs - bfs why? - need to check all avaliable paths
        # need to walk thr the tree, passing the curr depth,
        # then return the max of (left, right)

        if not root:
            return 0

        return max(self.walkthr(root.left, 1),self.walkthr(root.right, 1) )
