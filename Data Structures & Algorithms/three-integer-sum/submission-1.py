class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        first_i = 0
        res = []
        while first_i < len(nums) - 2:
            left, right = first_i + 1, len(nums) - 1
            while left < len(nums) and right > first_i and left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == -nums[first_i]:
                    res.append([nums[first_i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while right > first_i and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < -nums[first_i]:
                    left += 1
                else:
                    right -= 1
            first_i += 1
            while first_i < len(nums) - 2 and nums[first_i] == nums[first_i - 1]:
                first_i += 1
        return res
                    










    #     nums.sort()
    #     res, unique_set = [], set()
    #     for i in range(len(nums)):
    #         first_num = nums[i]
    #         two_nums = self.find_sum(nums, i + 1, len(nums) - 1, -first_num)
    #         if not len(two_nums):
    #             continue
    #         for two_nums_entry in two_nums:
    #             valid_triplets = tuple([first_num]) + two_nums_entry
    #             if valid_triplets not in unique_set:
    #                 res.append(list(valid_triplets))
    #                 unique_set.add(valid_triplets)
    #     return res
            
    # def find_sum(self, nums, left, right, target):
    #     two_nums_ls = []
    #     while left < right and left < len(nums) and right >= 0:
    #         cur_sum = nums[left] + nums[right]
    #         if cur_sum == target:
    #             two_nums_ls.append(tuple([nums[left], nums[right]]))
    #             left += 1
    #             right -= 1
    #         elif cur_sum < target:
    #             left += 1
    #         else:
    #             right -= 1
    #     return two_nums_ls