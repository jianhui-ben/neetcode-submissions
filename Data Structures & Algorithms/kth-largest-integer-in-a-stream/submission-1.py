import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        we only care about the top K large number
        since if a new number is smaller than the kth largest one, nothing change
        if a new number is bigger than the kth largest one, then pop the min one and add the new number
        """
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        cur_kth_large_val = self.minheap[0] if self.minheap else float("-inf")
        if val >= cur_kth_large_val:
            heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
            
        
