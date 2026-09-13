# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        iterative way (BFS with a queue)
        """
        if not root: return root
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root

        # """
        # recursion
        # """
        # if not root:
        #     return root
        
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root