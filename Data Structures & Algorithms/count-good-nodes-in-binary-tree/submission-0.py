# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        dfs to keep track the max node value up
        """
        self.out = 0
        def traverse(cur, cur_max):
            if not cur: return
            if cur.val >= cur_max:
                self.out += 1
                cur_max = cur.val
            traverse(cur.left, cur_max)
            traverse(cur.right, cur_max)
        traverse(root, float("-inf"))
        return self.out