# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        1. head on the preorder, num_root
        2. find the index of num_root in inorder, idx_root_in_order
        3. separate [0: idx_root_in_order], [idx_root_in_order + 1: -1] in in_order
        4. separate [1: idx_root_in_order + 1], [idx_root_in_order + 1 : -1] in pre_order
        5. recursion
        """
        self.stored_in_order = {val : i for i, val in enumerate(inorder)}
        self.preorder = preorder
        self.inorder = inorder


        def recursion(left_in_order, right_in_order, left_pre_order, right_pre_order):
            if left_in_order > right_in_order or left_pre_order > right_pre_order:
                return None
            
            
            head_val = self.preorder[left_pre_order]
            head = TreeNode(head_val)
            idx_head_in_order = self.stored_in_order[head_val]
            left_side_left_in_order, left_side_right_in_order = left_in_order, idx_head_in_order - 1
            right_side_left_in_order, right_side_right_in_order = idx_head_in_order + 1, right_in_order

            left_subtree_size = idx_head_in_order - left_in_order

            left_side_left_pre_order, left_side_right_pre_order = left_pre_order + 1, left_pre_order + left_subtree_size
            right_side_left_pre_order, right_side_right_pre_order = left_pre_order + left_subtree_size + 1, right_pre_order
            head.left = recursion(left_side_left_in_order, left_side_right_in_order, left_side_left_pre_order, left_side_right_pre_order)
            head.right = recursion(right_side_left_in_order, right_side_right_in_order, right_side_left_pre_order, right_side_right_pre_order)
            return head
        return recursion(0, len(inorder) - 1, 0, len(preorder) - 1)

        # if not preorder: return None
        # if len(preorder) == 1: return TreeNode(preorder[0])
        
        # head_val = preorder[0]
        # head = TreeNode(head_val)
        # idx_root_in_order = inorder.index(head_val)
        # left_inorder, right_inorder = inorder[0: idx_root_in_order], inorder[idx_root_in_order + 1:]
        # left_preorder, right_preorder = preorder[1: idx_root_in_order + 1], preorder[idx_root_in_order + 1 :]

        # head.left = self.buildTree(left_preorder, left_inorder)
        # head.right = self.buildTree(right_preorder, right_inorder)
        # return head





        