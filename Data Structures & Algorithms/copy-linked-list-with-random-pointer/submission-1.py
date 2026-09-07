"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        need a hashmap to store original node and copy
        """
        if not head: return None
        cur = head
        nodes_map = {}
        while cur:
            nodes_map[cur] = Node(x = cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                nodes_map[cur].next = nodes_map[cur.next]
            if cur.random:
                nodes_map[cur].random = nodes_map[cur.random]
            cur = cur.next
        return nodes_map[head]


        