# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        recursively check the upper and lower boundary for each node
        """
        self.out = True
        
        def traverse(cur, lower, upper):
            if not cur: return
            if not self.out: return
            if cur.val <= lower or cur.val >= upper:
                self.out = False
                return
            traverse(cur.left, lower, cur.val)
            traverse(cur.right, cur.val, upper)

        traverse(root, float("-inf"), float("inf"))
        return self.out