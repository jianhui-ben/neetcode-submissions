# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        fast & slow pointer
        """
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        while slow and fast:
            if slow == fast:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        return False