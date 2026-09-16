# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        basically for each depth, i need to find the most right node

        use a map to track {depth: node.val}
        recursion alway check the right child first, then middle, then left child

        time: O(n)
        space: O(n)
        """

        self.stored = {}
        def traverse(node, depth):
            if not node: return
            if depth not in self.stored:
                self.stored[depth] = node.val
            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)
        traverse(root, 0)
        out = []
        for i in range(len(self.stored)):
            out.append(self.stored[i])
        return out
        