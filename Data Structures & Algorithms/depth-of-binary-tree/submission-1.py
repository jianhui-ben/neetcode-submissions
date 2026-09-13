# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        iterative approach using a stack
        """
        if not root: return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            cur, cur_depth = stack.pop()
            max_depth = max(cur_depth, max_depth)
            if cur.left:
                stack.append((cur.left, cur_depth + 1))
            if cur.right:
                stack.append((cur.right, cur_depth + 1))
        return max_depth
        

        # """
        # depth first search
        # time: O(n)
        # space: O(n)
        # """
        # if not root: return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
