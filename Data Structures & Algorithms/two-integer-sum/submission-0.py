class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        we need index, so we can't sort
        
        brute force:
        nested for loop to for the first i and j combo:
        O(n^2) time and O(1) space

        
        faster solution:
        save every number and its index in a map m: {nums[i]: [i]}
        
        then traverse nums[j] where j is [0, len(nums))
        if (target - nums[j]) exist in map m:
            if (target - nums[j]) != nums[j]:
                then return (j, m[target - nums[j][0]])
            elif len(m[target - nums[j]) > 1:
                then return (j, m[target - nums[j][1]])
        
        time: O(n)
        space: O(n)
        """
        from collections import defaultdict
        value_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            value_to_indices[val].append(i)

        for j in range(len(nums)):
            if (target - nums[j]) in value_to_indices:
                if (target - nums[j]) != nums[j]:
                    return [j, value_to_indices[target - nums[j]][0]]
                elif len(value_to_indices[target - nums[j]]) > 1:
                    return [j, value_to_indices[target - nums[j]][1]]
        
        return None