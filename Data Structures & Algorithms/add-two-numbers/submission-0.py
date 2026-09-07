# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        recursion
        """
        def addTwo(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            
            carry, val_sum = (val_1 + val_2 + carry) // 10, (val_1 + val_2 + carry) % 10
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

            next_node = addTwo(l1, l2, carry)
            cur = ListNode(val_sum, next_node)
            return cur

        return addTwo(l1, l2, 0)