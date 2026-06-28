class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        worst case: On(n^2)

        Linear runtime solution of using two pointer:
        res = max(res, (right - left) * min(heights[left], heights[right])
        """
        left, right, res = 0, len(heights) - 1, 0
        while left < right:
            res =  max(res, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return res
            