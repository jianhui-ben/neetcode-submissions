class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking:
        
        for each i in nums:
            put it into the cur_list
            then continue to permutate with cur_list and the rest of candidates
            pop it from the cur_list
        time: N !
        space: O(1)
        """
        
        out = []
        len_nums = len(nums)
        def backtracking(cur_list, cur_candidates):
            if len(cur_list) == len(nums):
                out.append(list(cur_list))
                return

            for i in range(len_nums):
                if cur_candidates[i] == None:
                    continue
                cur_list.append(cur_candidates[i])
                cur_candidates[i] = None

                backtracking(cur_list, cur_candidates)
                cur_candidates[i] = cur_list.pop()

        backtracking([], nums)
        return out
