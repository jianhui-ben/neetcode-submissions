# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        recursion somehow for each node, to return the max path sum for the path ending at this node
        it's a recursion because you can just get max(recursion(node.left), recursion(node.right)) + node.val
        also you can choose not using the child subtreee at all
        meanwhile we record max(output, left path + right path + node.val)
        
        typical preorder depth first traversal
        time: O(n)
        space: O(n)
        """
        
        self.out = float("-inf")
        
        def max_path_sum_ending(cur):
            if not cur:
                return 0

            left_max_sum = max(0, max_path_sum_ending(cur.left))
            right_max_sum = max(0, max_path_sum_ending(cur.right))
            
            self.out = max(self.out, left_max_sum + right_max_sum + cur.val)
            return max(left_max_sum, right_max_sum) + cur.val
        max_path_sum_ending(root)
        return self.out