from collections import defaultdict
class LRUCache:

    class ListNode:
        def __init__(self, val = (0, 0), next = None, prev = None):
            self.val = val  
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        """
        a doubly linked list to keep the recency
        a hash map with key and the corresponding node
        """
        self.head = self.ListNode()
        self.tail = self.ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.stored = {}

    def insert_to_tail(self, cur_node):
        cur_tail = self.tail.prev
        cur_tail.next, cur_node.next = cur_node, self.tail
        cur_node.prev, self.tail.prev = cur_tail, cur_node

    def delete(self, cur_node):
        cur_prev, cur_next = cur_node.prev, cur_node.next
        cur_node.prev.next = cur_next
        cur_node.next.prev = cur_prev
        
    def get(self, key: int) -> int:
        if key not in self.stored:
            return -1

        target_node = self.stored[key]
        self.delete(target_node)
        self.insert_to_tail(target_node)
        return target_node.val[1]  

    def put(self, key: int, value: int) -> None:
        if key not in self.stored:
            target_node = self.ListNode((key, value))
            self.stored[key] = target_node
        else:
            target_node = self.stored[key]
            target_node.val = (key, value)
            self.delete(target_node)
        
        self.insert_to_tail(target_node)

        ## check if the cache is over the capacity
        if len(self.stored) > self.capacity:
            cur_head = self.head.next
            self.delete(cur_head)
            self.stored.pop(cur_head.val[0])
            
        
