class Solution:
    def trap(self, height: List[int]) -> int:
        """
        a better Space optimized two pointer solution
        """
        left, right, out = 0, len(height) - 1, 0
        left_max, right_max = height[left], height[right]
    
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                out += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                out += right_max - height[right]
                right -= 1
        return out
            

        # """
        # for any position i, keep the max num on i's left and i's right
        # the water trapped in i = min(max_nums[i]) - height[i]
        # """
        # left_max, right_max = [height[0]], [height[-1]]
        # for h in height[1:]:
        #     left_max.append(max(left_max[-1], h))
        # for h in reversed(height[:-1]):
        #     right_max.append(max(right_max[-1], h))
        # right_max = list(reversed(right_max))
        
        # out = 0
        # for i in range(len(height)):
        #     out += max(0, min(left_max[i], right_max[i]) - height[i])
        
        # return out