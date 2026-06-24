class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        option 1: convert list into a set, and 
        then compare the size of the list and set

        time: O(n)
        space: O(n)
        """
        # return len(set(nums)) != len(nums)


        """
        option 2: better space option
        we do sorting first, then compare nums[i] and nums[i+1] in place
        time: O(n log n)
        space: O(1)
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False




