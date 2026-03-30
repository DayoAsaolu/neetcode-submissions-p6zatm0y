# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, head):
        if not head:
            return
            
        head.left,head.right = head.right, head.left

        self.swap(head.left)
        self.swap(head.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # save the root tmp (need to return that)
        # recursively go thr the tree, swaping l & r
        # base conditon - if root.val

        head = root
        self.swap(root)
        return head