class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        in place swap

        because everything has to be in [1, n]
        each value switched to its v-1 th position
        until it find that position already got assigned the value
        in-line cyclic swap
        time: O(n), space: O(1)
        """
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            else:
                correct_idx = nums[i] - 1
                if nums[correct_idx] == nums[i]:
                    return nums[i]
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        return None
                
        