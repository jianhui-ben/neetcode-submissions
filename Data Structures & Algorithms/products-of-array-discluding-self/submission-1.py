class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        using division is very easy

        but we could also treat every output, 
        res[i] = product of nums[0] to nums[i - 1] * nums[i + 1] to nums[-1]
        for each res[i], we maintain two stacks:
        left_to_right[i] = product up to index i from left to right
        right_to_left[i] = product to index i from right to left

        res[i] = left_to_right[i - 1] * right_to_left[i + 1]
        
        edge case:
        i = 0: left_to_right should be 1
        i = len(nums) - 1: right_to_left should be 1
        so we could append one extra 1 to every head of the stack

        time: O(n)
        space: O(n)
        """
        # left_to_right, right_to_left = [1], [1]
        # for i in range(len(nums)):
        #     ## [1, 1, 2, 8, 48]
        #     left_to_right.append(nums[i] * left_to_right[-1])
        
        # for i in range(len(nums) - 1, -1, -1):
        #     ## [1, 6, 24, 48, 48]
        #     right_to_left.append(nums[i] * right_to_left[-1])

        # return [left_to_right[i] * right_to_left[len(nums) - i - 1] for i in range(len(nums))]
        
        """
        O(1) space optimization: inplace to save the prefix product or suffix product
        use the final res to hold the prefix product and then loop backward
        """
        res = [1 for _ in range(len(nums))]
        prefix_product = 1
        for i in range(len(res)):
            res[i] *= prefix_product
            prefix_product *= nums[i]
        
        prefix_product = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= prefix_product
            prefix_product *= nums[i]
        return res




