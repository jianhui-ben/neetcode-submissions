class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        if inflection point is on left of mid:
            then whole right part is sorted:
                if target is in the right part:
                    then left = mid + 1
                else:
                    right = mid - 1
        else:
            then whole left part is sorted:
                if target is in the left part:
                    then right = mid - 1
                else:
                    left = mid + 1
        we could return left boundary
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > nums[left]:
                if nums[left] == target: return left
                elif nums[left] < target < nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1
            else:
                if nums[right] == target: return right
                elif nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        if left < len(nums) and nums[left] == target:
            return left
        elif right >= 0 and nums[right] == target:
            return right
        return -1