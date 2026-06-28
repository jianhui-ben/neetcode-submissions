class Solution:
    def trap(self, height: List[int]) -> int:
        """
        for any position i, keep the max num on i's left and i's right
        the water trapped in i = min(max_nums[i]) - height[i]
        """
        left_max, right_max = [height[0]], [height[-1]]
        for h in height[1:]:
            left_max.append(max(left_max[-1], h))
        for h in reversed(height[:-1]):
            right_max.append(max(right_max[-1], h))
        right_max = list(reversed(right_max))
        
        out = 0
        for i in range(len(height)):
            out += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return out