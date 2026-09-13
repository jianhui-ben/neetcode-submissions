# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_len = 0
        def getDepth(cur):
            if not cur: return 0
            left_len = right_len = 0
            if cur.left:
                left_len = 1 + getDepth(cur.left)
            if cur.right:
                right_len = 1 + getDepth(cur.right)
            self.max_len = max(self.max_len, left_len + right_len)

            return max(left_len, right_len)
        getDepth(root)
        return self.max_len

        # """
        # recursion:
        # for each node, the diameter = left max depth + right max depth
        # time: O(n)
        # time: O(h)
        # """
        # self.max_len = 0

        # def getLeftAndRightDepth(cur):
        #     left_len, right_len = 0, 0
        #     if cur and cur.left:
        #         left_len = max(getLeftAndRightDepth(cur.left)) + 1
        #     if cur and cur.right:
        #         right_len = max(getLeftAndRightDepth(cur.right)) + 1
        #     self.max_len = max(self.max_len, left_len + right_len)
        #     return left_len, right_len
        # left_dep, right_dep = getLeftAndRightDepth(root)
        # return self.max_len