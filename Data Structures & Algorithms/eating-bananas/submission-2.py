class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        binary search:
        min: sum(piles) // h
        max: max(piles)

        how to know if this rate k can finish eat all the banas within h hours
        for each pile in piles: if sum(pile / k) >= h
        we need to find the first k that satisfy the above condition

        time: O(log (max - min) * len(piles)), roughly m * log(n), where m = 10^4 and n = 10^13
        space: O(1)
        """
        
        left, right = sum(piles) // h, max(piles)

        def eat_all_bananas(speed):
            if not speed: return False
            cur_time_spend = 0
            for pile in piles:
                if not pile % speed:
                    cur_time_spend += pile // speed
                else:
                    cur_time_spend += pile // speed + 1
                if cur_time_spend > h: return False
            return True
        
        while left <= right:
            mid = left + (right - left) // 2
            if (eat_all_bananas(mid)): 
                right = mid - 1
            else:
                left = mid + 1
        return left