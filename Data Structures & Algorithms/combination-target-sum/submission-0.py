class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        backtracking to try all the possiblities
        """

        out = []
        nums.sort()
        def backtracking(current_list, cur_target, start_idx):
            if not cur_target:
                out.append(list(current_list))
                return
            
            for i in range(start_idx, len(nums)):
                num = nums[i]
                if num > cur_target:
                    return
                current_list.append(num)
                backtracking(current_list, cur_target - num, i)
                current_list.pop()
        backtracking([], target, 0)
        return out
                
            