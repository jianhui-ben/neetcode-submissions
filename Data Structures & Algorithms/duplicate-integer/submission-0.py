class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        option 1: convert list into a set, and 
        then compare the size of the list and set

        time: O(n)
        space: O(n)
        """
        return len(set(nums)) != len(nums)