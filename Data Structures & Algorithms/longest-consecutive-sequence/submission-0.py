class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## use a map to see if the num + 1 exist exist or not
        ## if exist, then continue to explore, and mark that num as None
        
        import heapq
        distinct_nums = list(set(nums))
        heapq.heapify(distinct_nums)
        num_to_index = {v: i for i, v in enumerate(distinct_nums)}
        
        out = 0
        for i in range(len(distinct_nums)):
            num = distinct_nums[i]
            if num == None:
                continue
            cur_seq_len = 1
            distinct_nums[i] = None
            while (num + 1) in num_to_index:
                next_i = num_to_index[num + 1]
                distinct_nums[next_i] = None
                num += 1
                cur_seq_len += 1
            out = max(out, cur_seq_len)

        return out
                