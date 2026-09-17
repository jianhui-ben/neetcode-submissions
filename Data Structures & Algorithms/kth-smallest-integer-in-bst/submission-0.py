# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        in-order traverse
        """
        self.out = None
        self.n_th = 1
        
        def traverse(cur):
            if not cur: return
            traverse(cur.left)
            if self.out != None: return
            if self.n_th == k:
                self.out = cur.val
                return
            self.n_th += 1
            traverse(cur.right)

        traverse(root)
        return self.out