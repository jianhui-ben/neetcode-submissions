# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        fully balanced for each node
        each node abs(left depth - right depth) <= 1
        recursion to check if every node satisfied above condition
        while recursion itself return the depth of the node

        Time: O(n)
        space: O(h)
        """
        self.balanced = True
        
        def traverse(cur):
            if not self.balanced: return 0
            if not cur: return 0
            left_dep = right_dep = 0
            if cur.left:
                left_dep = traverse(cur.left) + 1
            if cur.right:
                right_dep = traverse(cur.right) + 1

            if abs(left_dep - right_dep) > 1:
                self.balanced = False
            
            return max(left_dep, right_dep)
                

        traverse(root)
        return self.balanced