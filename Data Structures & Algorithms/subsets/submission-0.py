class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        typical exhaustive enumeration uses backtracking
        O(N!)
        """
        
        out = []
        
        def backtracking(cur_set, start):
            out.append(list(cur_set))
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                cur_set.append(nums[i])
                backtracking(cur_set, i + 1)
                cur_set.pop()
            
        backtracking([], 0)
        return out