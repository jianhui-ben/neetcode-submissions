class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking:
        
        sort it first, so we could potentially skip duplicate subsets

        backtrack(cur_list, start_idx)
        """

        nums.sort()
        out = []
        
        def backtracking(cur_list, start_idx):
            out.append(list(cur_list))
            if start_idx >= len(nums):
                return

            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue
                cur_list.append(nums[i])
                backtracking(cur_list, i + 1)
                cur_list.pop()

        backtracking([], 0)

        return out
        
        