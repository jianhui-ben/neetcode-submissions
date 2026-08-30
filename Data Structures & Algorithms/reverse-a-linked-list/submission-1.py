# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # ## recursive way
        # if not head or not head.next:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        ## iterative way
        prev, cur = None, head
        while cur:
            next_cur = cur.next
            cur.next = prev
            prev = cur
            cur = next_cur
        return prev

        