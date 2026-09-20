import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        target = len(nums) - k
        
        for _ in range(target):
            heapq.heappop(nums)
        return nums[0]
        
        
        