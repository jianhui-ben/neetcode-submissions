class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        monotonic stack is the most optimal solution, better than sliding window
        
        we maintain a stack, where stack[0] store the index of the max num in the current window
        when we move to the right, we insert the right to the monotonic stack's tail, and pop out
        any index whose number is smaller
        """
        from collections import deque
        stack, out = deque(), []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)

            while stack and stack[0] <= i - k:
                stack.popleft()
            
            if i >= k - 1:
                out.append(nums[stack[0]])

        return out





        # """
        # we need a max heap to track which number is the max, if that number is removed,
        # then it's O(1) to know the second largest number in the window
        # Meanwhile we also need to track the last index of each number in the heap
        # so we know if that max number is valid inside the current window

        # we record each maxHeap's head when the window is valid and the head is valid inside the window

        # time: len(nums) * log k
        # space: O(k)
        # """
        # import heapq
        # left = right = 0
        # out = []
        # max_heap = []
        # while right < len(nums):
        #     heapq.heappush(max_heap, (-nums[right], right))
        #     right += 1
            
        #     while right - left > k:
        #         left += 1
            
        #     if right - left == k:
        #         while max_heap[0][1] < left:
        #             heapq.heappop(max_heap)

        #         out.append(-max_heap[0][0])

        # return out

        
        

        
        
        
        
