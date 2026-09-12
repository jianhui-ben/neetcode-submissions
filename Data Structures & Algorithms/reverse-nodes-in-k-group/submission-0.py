# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        recursion:
            for each k do a recursion

        how to reverse:
            do a iterative way
        
        time: O(n)
        space: O(n/k)
        """
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next
        

        ## reverse first k
        cur = head
        prev = None
        for _ in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        head.next = self.reverseKGroup(cur, k)
        return prev
        

            