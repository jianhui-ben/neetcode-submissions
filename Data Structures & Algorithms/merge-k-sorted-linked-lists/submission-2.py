# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        """
        min heap
        time: O (n log k)
        space: O(k)
        """
        lists = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(lists)
        cur = dummy = ListNode()
        while lists:
            _, i, node = heapq.heappop(lists)
            cur.next = node
            if node.next:
                heapq.heappush(lists, (node.next.val, i, node.next))
            cur = cur.next
        return dummy.next
            
            
        





        # """
        # brute force
        # recursion + save
        # k linked lists, and total n nodes
        # time: O(n * k log k)
        # space: O(n) 
        # """
        # lists = [node for node in lists if node]
        # if not lists:
        #     return None
        
        # # lists.sort(key=lambda node: node.val)
        # lists.sort(key=lambda node: (node.val, id(node)))
        # head = ListNode(lists[0].val)
        # if lists[0].next:
        #     lists[0] = lists[0].next
        # else:
        #     lists.pop(0)
        # head.next = self.mergeKLists(lists)
        # return head            