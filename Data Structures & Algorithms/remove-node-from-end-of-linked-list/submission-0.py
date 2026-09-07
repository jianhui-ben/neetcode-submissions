# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        get total length tot_len
        and remove the tot_len - n th one
        """
        
        tot_len = 0
        cur = head
        while cur:
            tot_len += 1
            cur = cur.next

        temp = ListNode()
        temp.next = head
        cur = temp
        for _ in range(tot_len - n):
            cur = cur.next
        cur.next = cur.next.next
        return temp.next



