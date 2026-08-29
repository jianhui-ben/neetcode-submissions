class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        need to find the last number greater than nums[0], its left is the answer
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        if right == len(nums) - 1: return nums[0]
        else: return nums[right + 1]