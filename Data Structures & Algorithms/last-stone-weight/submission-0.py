
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        heapq to simulate
        """
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        
        while len(maxheap) > 1:
            a, b = heapq.heappop(maxheap), heapq.heappop(maxheap)
            new_stone = a - b
            if new_stone:
                heapq.heappush(maxheap, new_stone)
        
        return 0 if not maxheap else -maxheap[0]
        
        