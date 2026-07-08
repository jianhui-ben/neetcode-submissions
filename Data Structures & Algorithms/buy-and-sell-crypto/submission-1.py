class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sliding window:
        first find a highest price as right, and then shrink the left to find the smallest
        buying point
        """

        left, right = 0, 1
        out = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                out = max(out, prices[right] - prices[left])
            else:
                left = right 
            right += 1
        return out
            