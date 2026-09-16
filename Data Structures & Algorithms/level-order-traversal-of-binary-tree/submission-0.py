# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS with a queue
        """
        if not root: return []
        level = [root]
        out = []
        while level:
            new_level = []
            cur_level = []
            for node in level:
                if not node: continue
                cur_level.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            out.append(cur_level)
            level = new_level
        return out
