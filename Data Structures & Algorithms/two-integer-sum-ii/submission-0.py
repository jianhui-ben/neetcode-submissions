class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two pointer
        
        left and right index: right = len(numbers) -1

        keep tracking cur_sum = numbers[left] + numbers[right]
        if cur_sum == target: return [left + 1, right + 1]
        if cur_sum < target: left += 1
        if cur_sum > target: right -= 1
        return [left + 1, right + 1]
        """

        left, right = 0, len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
        