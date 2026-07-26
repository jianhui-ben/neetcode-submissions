class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        keep a descreasing monotonic stack to keep track on the past day's temperature

        when temperatures[i] is larger, any previous date j's temperature can be popped
        from the stack, since we can just record how many i - j for output[j]
        
        time: O(n)
        space: O(n)
        """
        stack, out = [], [0 for _ in range(len(temperatures))]
        
        for i, temp in enumerate(temperatures):
            
            while stack and stack[-1][1] < temp:
                prev_date, prev_temp = stack.pop()
                out[prev_date] = i - prev_date
            stack.append((i, temp))
        
        return out