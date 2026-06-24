class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        return [val for val, _ in sorted(counter.items(), key = lambda item: -item[1])[:k]]