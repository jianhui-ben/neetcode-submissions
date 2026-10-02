class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtracking
        """
        candidates.sort()

        out = []

        def backtracking(cur_list, target, start_idx):
            if not target:
                out.append(list(cur_list))
                return
            
            if start_idx == len(candidates): return
            for i in range(start_idx, len(candidates)):
                ## skip the index where candidates[i] == candidates[i - 1]
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                if num > target:
                    return
                
                cur_list.append(num)
                backtracking(cur_list, target - num, i + 1)
                cur_list.pop()

        
        backtracking([], target, 0)

        return out