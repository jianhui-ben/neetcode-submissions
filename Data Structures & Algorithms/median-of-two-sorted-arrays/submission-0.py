class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ## better add a padding on both head
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = [-float("inf")] + nums1 + [float("inf")]
        nums2 = [-float("inf")] + nums2 + [float("inf")]
        target_len = (len(nums1) + len(nums2)) // 2
        
        left, right = 0, min(target_len - 1, len(nums1) - 1)

        def get_median(nums1_mid, nums2_idx):
            print(len(nums1), len(nums2))
            if (len(nums1) + len(nums2)) % 2:
                # print("it's an odd")
                return float(min(nums1[nums1_mid + 1], nums2[nums2_idx + 1]))
            else:
                # print("it's an even")
                return (max(nums1[nums1_mid], nums2[nums2_idx]) + min(nums1[nums1_mid + 1], nums2[nums2_idx + 1])) / 2
        # print(f"nums1: {nums1}, nums2: {nums2}")
        while left <= right:
            nums1_mid = left + (right - left) // 2
            nums2_idx = target_len - (nums1_mid + 1) - 1
            # print(f"nums1_mid: {nums1_mid}, nums2_idx: {nums2_idx}")

            # check if nums1[i1] <= nums2[i2 + 1] and nums2[i2] <= nums1[i1 + 1]
            if (nums2_idx == len(nums2) - 1 or nums1[nums1_mid] <= nums2[nums2_idx + 1]) and (nums1_mid == len(nums1) - 1 or nums2[nums2_idx] <= nums1[nums1_mid + 1]):
                return get_median(nums1_mid, nums2_idx)
            elif nums2_idx < len(nums2) - 1 and nums1[nums1_mid] > nums2[nums2_idx + 1]:
                # nums1_mid need to move to the left part of nums1
                right = nums1_mid - 1
            elif nums1_mid < len(nums1) - 1 and nums2[nums2_idx] > nums1[nums1_mid + 1]:
                #nums1_mid need to move to the right part of nums1
                left = nums1_mid + 1
        return None





        """
        idea is to do the binary search on the shorter nums:


        assuming we want to find len(total) // 2
        
        nums1 is the shorter array

        nums1[0], nums1[1], nums1[2], nums1[3] ...  nums1[-1]

        <------------ a right median index i1 ------------------->
        
        then on nums2, we know the index i2 should be len(total) // 2 - i + 1
        
        nums1[0: i+1] (i+1 elements) + nums2[0: ]


        nums1: [1, 2, 3]
        nums2: [1, 3, 4, 6, 8, 9]

        9 elements -> find 4 element on the left
        
        binary search: 
        nums1 need to find 4 // 2 = 2 elements
        mid index i1 = 2 - 1 = 1
        [1, 2, 3]
            ^
        
        nums2 need to find 4 - 2 = 2
        nums2 index i2 = 2 - 1 = 1
        [1, 3, 4, 6, 8, 9]
            ^
        need to check if nums1[i1] <= nums2[i2 + 1] and nums2[i2] <= nums1[i1 + 1]
        if yes -> since it's odd toal number -> we return min(nums1[i1 + 1], nums2[i2+ 1])
        if no -> we start the search

        check if nums1[i1] <= nums2[i2 + 1] and nums2[i2] <= nums1[i1 + 1]

        case 1: 
        if nums1[i1] > nums2[i2 + 1]:
        nums1: [1, 3, 3]
                   ^
        nums2: [1, 2, 2, 6, 8, 9]
                   ^
        we should update the right boundary on our search in nums1:
        right = mid - 1
        left = right = mid index = 0
        nums1: [1, 3, 3]
                ^
        nums2: [1, 2, 2, 6, 8, 9]
                      ^
        check if nums1[i1] <= nums2[i2 + 1] and nums2[i2] <= nums1[i1 + 1]
        then return min(3, 6) -> 3

        case 2: 
        if nums2[i2] > nums1[i1 + 1]:
        nums1: [1, 2, 3]
                   ^
        nums2: [1, 4, 4, 6, 8, 9]
                   ^
        left = mid + 1 = 2
        right = 2
        new mid = 2
        nums1: [1, 2, 3]
                      ^
        nums2: [1, 4, 4, 6, 8, 9]
                ^
        check if nums1[i1] <= nums2[i2 + 1] and nums2[i2] <= nums1[i1 + 1]
        then return min(4, infinity) -> 4
        """
        


