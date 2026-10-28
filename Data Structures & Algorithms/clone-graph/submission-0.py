"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        recursion + hashmap to map the old_node to its copy
        """
        
        hashmap = {}

        def copyNode(node):
            if not node: return None
            if node in hashmap:
                return hashmap[node]
            
            new_node = Node(node.val)
            hashmap[node] = new_node
            new_neighbors = []
            for neighbor_node in node.neighbors:
                new_neighbor_node = copyNode(neighbor_node)
                new_neighbors.append(new_neighbor_node)
            new_node.neighbors = new_neighbors
            return new_node

        return copyNode(node)