import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        keep a minheap to keep k closest points
        """
        minheap = [(point[0] ** 2 + point[1] ** 2, point[0], point[1]) for point in points]
        heapq.heapify(minheap)
        out = []
        for _ in range(k):
            _, x, y = heapq.heappop(minheap)
            out.append([x, y])
        return out
