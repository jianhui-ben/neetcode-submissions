# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        first split into two half
        reverse the second half
        then merge two parts
        """
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        cur, prev = slow.next, None
        slow.next = None
        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next
        
        first_half, second_half = head, prev
        
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2
        return None
