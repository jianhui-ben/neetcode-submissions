class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # counter = Counter(nums)
        # return [val for val, _ in sorted(counter.items(), key = lambda item: -item[1])[:k]]

        
        """
        bucket sort
        """
        from collections import Counter
        counter = Counter(nums)
        # avoid this trap of using occurences = [set()] * (len(nums) + 1)
        occurences = [set() for _ in range(len(nums) + 1)]
        for num, cnt in counter.items():
            occurences[cnt].add(num)
        
        res = []
        for i in range(len(occurences) - 1, -1, -1):
            for num in occurences[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return None