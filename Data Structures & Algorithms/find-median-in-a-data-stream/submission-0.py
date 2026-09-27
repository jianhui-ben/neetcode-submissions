import heapq
class MedianFinder:

    """
    two parts
    [smaller part heap_0, max heap] [larger part heap_1 - min heap]
    try to make these two part equal or close in size, where smaller can be 1 number   larger size than larger part 
    given number n  
    check if n belong to which part
    [1], []
    2
    if a number is > median: assign to the second part
    [1], [2]
    
    3
    
    3 > 1 -> 
    
    [1], [2, 3]
    
    second part is longer, need to rebalance
    [2, 3] pop [2] to the first part

    addNum: O(log n)
    find median: O(1)
    """

    def __init__(self):
        self.max_heap, self.min_heap = [], []
        self.tot_len = 0
        
    def addNum(self, num: int) -> None:
        self.tot_len += 1
        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        while (len(self.max_heap) - len(self.min_heap)) not in {0, 1}:
            if (len(self.max_heap) > len(self.min_heap)):
                ## move number from 1st part to 2nd part:
                num = - heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num)
            else:
                ## move number from 2nd part to 1st part:
                num = - heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, num)
    

    def findMedian(self) -> float:
        if self.tot_len % 2:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0

        
        