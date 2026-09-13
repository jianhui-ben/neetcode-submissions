# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        dps check each node
        """
        if not p and not q: return True
        if not p and q: return False
        if not q and p: return False
        
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        m = # of nodes in root, n = # of nodes in subRoot
        time: O(m * n)
        space: O(m + n)

        """
        if root and subRoot and root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        left_match, right_match = False, False
        if root.left:
            left_match = self.isSubtree(root.left, subRoot)
        if root.right:
            right_match = self.isSubtree(root.right, subRoot)
        return left_match or right_match

        