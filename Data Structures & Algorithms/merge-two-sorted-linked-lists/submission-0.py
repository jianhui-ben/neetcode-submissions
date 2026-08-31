# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        add a fake head and then have a two pointer
        """
        
        new_head = ListNode()
        cur_head = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                cur_head.next = list1
                list1 = list1.next
            else:
                cur_head.next = list2
                list2 = list2.next
            cur_head = cur_head.next
        if list1:
            cur_head.next = list1
        elif list2:
            cur_head.next = list2
        return new_head.next
