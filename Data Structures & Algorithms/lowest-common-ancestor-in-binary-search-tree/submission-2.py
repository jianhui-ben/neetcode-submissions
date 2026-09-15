# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        a simplified recursion approach
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


        # """
        # dfs somehow
        # if cur node  == either p or q: return cur node
        # if p < cur node < q: return cur node
        # if cur < both p and q: cur = cur.right
        # elif cur > both p and q: cur = cur.right

        # time: O(h)
        # space: O(h)
        # """
        
        # self.out = None
        # if p.val > q.val:
        #     p, q = q, p
        # def traverse(cur):
        #     if not cur: return
        #     if cur.val == p.val or cur.val == q.val:
        #         self.out = cur
        #         return
        #     if p.val < cur.val < q.val:
        #         self.out = cur
        #         return
        #     if p.val < q.val < cur.val:
        #         traverse(cur.left)
        #     if cur.val < p.val < q.val:
        #         traverse(cur.right)
        #     return
        # traverse(root)
        # return self.out
