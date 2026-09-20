# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        pre_order = []
        def dfs(cur):
            if not cur: 
                pre_order.append("#")
                return
            pre_order.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return ",".join(pre_order)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pre_order = data.split(",")
        self.idx = 0
        def dfs():
            if self.idx >= len(pre_order) or pre_order[self.idx] == "#":
                self.idx += 1
                return None
            cur = TreeNode(int(pre_order[self.idx]))
            self.idx += 1
            cur.left = dfs()
            cur.right = dfs()
            return cur
        return dfs()
            




